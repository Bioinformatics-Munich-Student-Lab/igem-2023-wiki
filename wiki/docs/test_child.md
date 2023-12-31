## Polypharmacy Dataset
We illustrated 2 datasets that provide information about polypharmacy. 

The first dataset uses a preprocessed train and test dataset, provided within the Decagon paper [^1]. The dataset incorporates human protein-protein interaction networks, side effect data, and drug-target interactions, all compiled from different sources. Which contains drug-drug interactions in polypharmacy for side effect prediction.


Second dataset uses NSIDES [^2] project data, which includes data for drug side effects (OFFSIDES) and drug-drug pair side effects (TWOSIDES). These data represent an update from the data released to include adverse events reported to the FDA through database FDA Adverse Event Reporting System (FAERS) up to and including 2014, that contains information on adverse event and medication error. The dataset incorporates clinical reports with the taken drugs with their side effects, which in the report contains 1 to 49 drug combination with their side effects. 

### Quality Control and Dataset Splitting 
Repots contain drugs with no matched STITCH id or not able to extract the chemical structure embedding are filtered out. After quality control, the dataset is splited into train, validation, and test set in 0.8, 0.1, 0.1 ratio respectively by the report ids.

### Preprocessed Dataset

|                                          | Decagon | Nsides  |
|------------------------------------------|---------|---------|
| Number of Drugs                          | 645     | 2204    |
| Number of Side Effects                   | 963     | 17552   |
| Max number of Drug Combinations          | 2       | 10      |
| Polypharmacy Interactions for Training   | 4512911 | 2878989 |
| Polypharmacy Interactions for Validation | None    | 357294  |
| Polypharmacy Interactions for Testing    | 19842   | 357301  |
| Drug-Protein Interactions                | 18690   | None    |
| Protein-Protein Interactions             | 715612  | None    |


## Graph Structure
We construct a knowledge graph (KG). The graph consists of nodes of two types, drugs and hypernodes. The edges of the graph correspond to different drug combinations. The node feature of the drugs are based on chemical structures, and each hypernode feature signifies the side effects.

## Chemical Structure Embeddings

The chemical structure embeddings are extracted using MOLFORMER, a large-scale chemical language representations to capture molecular structure and properties published by IBM. Which employs a linear attention mechanism, coupled with highly distributed training, on    sequences of 1.1 billion unlabelled molecules from the PubChem and ZINC datasets

The chemical language embedding were extracted for Nsides dataset, the SMILES of the drugs were used to generate the embedding to provide biological meaningful information.  


## Model Architecture

The model architecture, named SEPIA (Side Effect Prediction with Interaction Awareness), is designed for drug interaction and side effect prediction, leveraging the graph representation of polypharmacy data. The model consists of an Encoder and a Decoder.

### Encoder:
* **Input**: \
Graph representation of the biological data, including drugs, proteins, and their interactions, along with identified side effects. 

* **Output**: \
Embeddings representing the interactions and effects. 

* **Architecture**: \
Consists of SAGEConv instances for processing heterogeneous graph data, and an embedding layer for side effects.

```python title='encoder' linenums="44"
class Encoder(nn.Module):
    def __init__(self, emb_dim, n_effects, n_hops):
        super(Encoder, self).__init__()

        self.effect_emb = nn.Embedding(n_effects, emb_dim)
        nn.init.xavier_uniform_(self.effect_emb.weight.data)

        self.layers = nn.ModuleList(
            GraphLayer(SAGEConv, emb_dim) for _ in range(n_hops)
        )
        self.act = F.relu

    def forward(self, graph_x, edge_index, x_nodes, effect_ids):
        for layer in self.layers:
            graph_x = layer(graph_x, edge_index)
            graph_x = {key: self.act(x) for key, x in graph_x.items()}

        #print(self.effect_emb)
        #print(self.effect_emb.num_embeddings)
        #print(effect_ids)
        embs = [graph_x['drugs'][nodes] + self.effect_emb(effect) for effect, nodes in zip(effect_ids, x_nodes)]
        return embs
```

### Decoder: 
* **Input**: \
Embeddings from the encoder. 

* **Output**: \
Predicted side effects in the form of a probability distribution between 0 and 1. 

* **Architecture**: \
A neural network that maps embeddings to side effect predictions.

```python title="sepia.py"
class First(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, *args):
        if type(x) == tuple:
            return x[1]
        else:
            return torch.zeros(x.shape)

class Sequential(nn.Sequential):
    def forward(self, *inputs):
        x = inputs[0]
        edge_index = inputs[1]
        for module in self._modules.values():
            x = module(x, edge_index)
        return x 
    

class GraphLayer(nn.Module):
    def __init__(self, layer, emb_dim):
        super().__init__()
        self.conv = Sequential(
            #Change order (might make more sense if only hypernode is updated first, then the rest)
            HeteroConv({
                ('proteins', 'protein_protein', 'proteins'): layer((-1, -1), emb_dim),
                ('drugs', 'drug_protein', 'proteins'): layer((-1, -1), emb_dim),
                ('drugs', 'hyperedge_part_1', 'hypernodes'): layer((-1, -1), emb_dim),
                ('hypernodes', 'hyperedge_part_2', 'drugs'): First(),
            }, aggr='sum'),
            #potentially add activation function
            HeteroConv({
                ('proteins', 'protein_protein', 'proteins'): First(),
                ('drugs', 'drug_protein', 'proteins'): First(),
                ('drugs', 'hyperedge_part_1', 'hypernodes'): First(),
                ('hypernodes', 'hyperedge_part_2', 'drugs'): layer((-1, -1), emb_dim),
            }, aggr='sum')
        )
        
    def forward(self, x, edge_index):
        x = self.conv(x, edge_index)
        return x

class Encoder(nn.Module):
    def __init__(self, emb_dim, n_effects, n_hops):
        super(Encoder, self).__init__()

        self.effect_emb = nn.Embedding(n_effects, emb_dim)
        nn.init.xavier_uniform_(self.effect_emb.weight.data)

        self.layers = nn.ModuleList(
            GraphLayer(SAGEConv, emb_dim) for _ in range(n_hops)
        )
        self.act = F.relu
        
    def forward(self, graph_x, edge_index, x_nodes, effect_ids):
        for layer in self.layers:
            graph_x = layer(graph_x, edge_index)
            graph_x = {key: self.act(x) for key, x in graph_x.items()}
        
        #print(self.effect_emb)
        #print(self.effect_emb.num_embeddings)
        #print(effect_ids)
        embs = [graph_x['drugs'][nodes] + self.effect_emb(effect) for effect, nodes in zip(effect_ids, x_nodes)]
        return embs

class Decoder(nn.Module):
    def __init__(self, emb_dim):
        super(Decoder, self).__init__()
        self.Sigmoid = nn.Sigmoid()
        self.Linear = nn.Linear(emb_dim, 1)

    def forward(self, embs):
        embs = torch.stack([torch.prod(x, dim=0) for x in embs])
        return self.Sigmoid(self.Linear(embs))

class SEPIA(nn.Module):
    def __init__(self, emb_dim, n_effects, n_hops):
        super(SEPIA, self).__init__()
        self.encoder = Encoder(emb_dim, n_effects, n_hops)
        self.decoder = Decoder(emb_dim)

    def forward(self, graph, x_nodes, effect_ids):
        graph_x = graph.x_dict
        edge_index = graph.edge_index_dict
        return self.decoder(self.encoder(graph_x, edge_index, x_nodes, effect_ids))
```


### Negative Sampler:

* **Functionality**: \
Generate negative samples (Random Side effects) for training the SEPIA mode.

## Training Description

The training involves both the training of the SEPIA model and the negative sampler for negative sampling. The MLPgenerator generates negative samples to compare with the positive sample for SEPIA to learn.  The process is iterative, optimizing the model's parameters to better predict the side effects of drug interactions.

### Step by Step: 

**1. Graph Building**: \
Construct the graph from the provided data, including drugs, proteins, and their interactions.
Data Loading: Utilizes a customized data loader (HyperNodeLoader) to prepare batches of data for training.

**2. Negative Sampling**: 
\An alternative approach to generate negative samples randomly.


**3. Forward Pass**: 
\The SEPIA model takes the graph data, processes it through the encoder to get embeddings, and then through the decoder to get side effect predictions.

**4. Loss Computation**: 
\Computes the loss using a binary cross-entropy loss function, considering both positive and negative samples.
Backpropagation: Gradients are calculated and the model's parameters are updated using an optimizer.

**5. Testing**: \
The model is evaluated on the test data, where it predicts side effects for given interactions.
Metrics Calculation: Calculates metrics like ROC AUC to evaluate the model's performance.

**6. Visualization**: \
Plots the ROC curve for both training and testing data to visualize the model's performance.


### Key Features:
**Polypharmacy Modelling**: \
The data structure is designed to handle interactions between n drugs with O(n) edges.  

**Heterogeneous Graph Processing**: \
The model can handle graphs with multiple types of nodes and edges, making it suitable for complex biological data.

**Negative Sampling**: \
Enhances the training process by generating negative samples.

**Modular Architecture**:\
 The separation of encoder and decoder allows for flexibility and adaptability to different data and tasks.

## Results

| Metrics/Dataset | Decagon | Nsides |
|-----------------|---------|--------|
| AUROC           | 0.95    | 1      |
| AUPRC           | 1       | 1      |

### Confusion matrix 


## References

[^1]: Marinka Zitnik, Monica Agrawal, Jure Leskovec, Modeling polypharmacy side effects with graph convolutional networks, Bioinformatics, Volume 34, Issue 13, July 2018, Pages i457–i466, https://doi.org/10.1093/bioinformatics/bty294

[^2]: Vanguri, Rami; Romano, Joseph; Lorberbaum, Tal; Youn, Choonhan; Nwankwo, Victor; Tatonetti, Nicholas (2017). nSides: An interactive drug--side effect gateway. figshare. Dataset. https://doi.org/10.6084/m9.figshare.5483698.v2

[^3]: David Weininger. 1988. SMILES, a chemical language and information system. 1. introduction to methodology and encoding rules. J. Chem. Inf. Comput. Sci. 28, 1 (February 1988), 31–36. https://doi.org/10.1021/ci00057a005