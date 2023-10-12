## Polypharmacy Dataset
We illustrated 2 datasets that provide information about polypharmacy. 

The first dataset is a preprocessed train/test/validation dataset, provided within the Decagon paper [^1]. The dataset incorporates human drug-drug interaction networks with side effects as indication of polypharmacy interactions, all compiled from different sources. 

Second dataset uses data from NSIDES [^2] project databank, which includes data for drug side effects (OFFSIDES) and drug-drug pair side effects (TWOSIDES). These data represent an update from the data released to include adverse events reported to the FDA through database FDA Adverse Event Reporting System (FAERS) up to and including 2014, that contains information on adverse event and medication error. The dataset incorporates clinical reports with the taken drugs with their side effects, which in the report contains 1 to 49 drug combinations with reported side effects.

### Dataset Preprocessing

#### Dacagon Dataset

This dataset is already preprocessed, details see [^4]

#### Nsides Dataset

1. **Extract Chemical Structure Embeddings**

We downloaded the entire STITCH databank version 5.0 with the names and SMILES strings of STITCH's chemicals. The the SMILES were canonicalized before the extraction of the chemical structure embeddings from MolFolmer (cite needed), chemicals are filtered when the extracted embeding is NA. Thus, we stored STITCH id, drug names and their chemical embedding into a table.

2. **Map Drug Names from Nsides with STITCH id**

The drug concept name from Nsides dataset were mapped with the drug names from the table with STITCH id, drug names and their chemical embedding. Drugs that can't be mapped are filtered. Thus, we stored the processed drug category from Nsides with STITCH id, drug names and their chemical embedding into a table.

3. **Quality Control and Dataset Splitting**

In quality contrial, report ids that contains any drugs that is not in our drug category are removed and we selected reports with 2 to 10 drug combination usage. After quality control, the dataset is splited into train, validation, and test set in 0.8, 0.1, 0.1 ratio respectively by the report ids.



### Preprocessed Dataset

|                                          | Decagon | Nsides  |
|------------------------------------------|---------|---------|
| Number of Drugs                          | 645     | 2204    |
| Number of Side Effects                   | 963     | 17552   |
| Max number of Drug Combinations          | 2       | 10      |
| Polypharmacy Interactions for Training   | 4512911 | 2878989 |
| Polypharmacy Interactions for Validation | 19785   | 357294  |
| Polypharmacy Interactions for Testing    | 19842   | 357301  |


## Graph Structure

We construct a knowledge graph (KG). The graph consists of nodes of two types, drugs and hypernodes. The edges of the graph correspond to different drug combinations. The node feature of the drugs are based on chemical structures, and each hypernode feature signifies the side effects.

## Chemical Structure Embeddings

The chemical structure embeddings are extracted using MOLFORMER, a large-scale chemical language representations to capture molecular structure and properties published by IBM. Which employs a linear attention mechanism, coupled with highly distributed training, on sequences of 1.1 billion unlabelled molecules from the PubChem and ZINC datasets. The chemical language embedding were extracted for Nsides dataset, the SMILES of the drugs were used to generate the embedding to provide biological meaningful information.  

## Intro to SEGEConv



## Hetrograph Construction

### Nodes

* **Drugs**: Represent the drugs with chemical structure embedding. \

* **Hypernodes**: Represented the polypharmacy cases, these nodes store aggregated information of side effects caused by drug combinations.


### Edges

* **Hyperedge Part 1**: Directed edges connecting drug nodes to hypernodes, indicating that a certain combination of drugs is associated with specific side effects stored in the hypernodes.

* **Hyperedge Part 2**: Directed edges connecting hypernodes back to drug nodes. These edges, in conjunction with Hyperedge Part 1, form hyperedges that encapsulate the relationships between drug combinations and their side effects.


```plaintext
    Drug1  Drug2  Drug3  
     (O)    (O)    (O)
        \    |    /
         \   |   /
          \  |  /
        [Hypernode 1]
(): Drugs
 |: Hyper edges
[]: Hypernode

```


```python
def build_graph(path: str, load_graph = True) -> HeteroData:
    
    # load graph if already created
    if os.path.exists(f"{path}/graph.pk") and load_graph:
        with open(f"{path}/graph.pk", "rb") as f:
            graph = pk.load(f)
        return graph

    SIDE_EFFECT_PATH = os.path.join(path, "side_effects.csv")
    DRUGS_PATH = os.path.join(path, "drugs.csv")
    POLYPHARMACY_PATH = os.path.join(path, "polypharmacy.csv")
    
    # load data
    side_effects = pd.read_csv(SIDE_EFFECT_PATH, skiprows=1, header=None)
    
    drugs = pd.read_csv(DRUGS_PATH, skiprows=1, header=None)
    drugs["features"] = drugs[drugs.columns[2:]].values.tolist()
    drugs = drugs[[0, "features"]]

    graph = HeteroData({
        "drugs": {'x': torch.tensor(drugs["features"]).to(torch.float32), "label": drugs[0]},
    })

    graph["drugs"].num_nodes = len(drugs)

    polypharmacy = pl.read_csv(POLYPHARMACY_PATH).to_pandas()
    polypharmacy_drugs = polypharmacy.iloc[:,0].str.split('|', expand=True)
    #add colnames polypharmacy, side_effects
    polypharmacy.columns = ['drug_combination', 'side_effect']

    #get max value in side_effect
    max_side_effect = side_effects[1].max()

    # apply name to index for all drugs on polypharmacy_drugs    
    for i in range(len(polypharmacy_drugs.columns)):
        polypharmacy_drugs[i] = name_to_index(graph["drugs"], polypharmacy_drugs[i])

    # Convert the DataFrame to a NumPy array
    polypharmacy_drugs_np = polypharmacy_drugs.to_numpy()

    # Use a list comprehension to convert each row of the NumPy array to a list, 
    # while filtering out NaN values
    polypharmacy[0] = [row[~np.isnan(row)].tolist() for row in polypharmacy_drugs_np]

    # sort the values in each row to make sure the same drug combinations are grouped together
    # Using list comprehension for speed improvement
    polypharmacy["drug_combination"] = ['|'.join(map(str, sorted(filter(pd.notna, row)))) 
                                        for row in polypharmacy_drugs.values]

    # Group by 'drug_combination' and aggregate the 'side_effect' values into lists and reset the index
    polypharmacy_grouped = polypharmacy.groupby('drug_combination')['side_effect'].apply(list).reset_index()

    # sort the values in the side_effect column of each row
    polypharmacy_grouped["side_effect"] = np.sort(polypharmacy_grouped["side_effect"].to_numpy())


    # Step 1: Extract indices where the matrix should have ones
    rows = []
    cols = []
    for i, side_effects in enumerate(polypharmacy_grouped["side_effect"]):
        rows.extend([i] * len(side_effects))
        cols.extend(side_effects)

    # Step 2: Create a COO matrix using these indices
    data = np.ones(len(rows))
    side_effect_matrix = coo_matrix((data, (rows, cols)), shape=(len(polypharmacy_grouped), max_side_effect + 1))

    # Step 3: Convert the COO matrix to a PyTorch sparse tensor if needed
    i = torch.LongTensor(np.vstack((side_effect_matrix.row, side_effect_matrix.col)))
    v = torch.FloatTensor(side_effect_matrix.data)
    shape = torch.Size(side_effect_matrix.shape)

    side_effect_tensor = torch.sparse.FloatTensor(i, v, shape)

    # add values in hypernodes.x of the graph for message passing
    graph["hypernodes"].x = side_effect_tensor.to(torch.float32)
    graph["hypernodes"].effect_ids = [torch.tensor(item) for item in polypharmacy_grouped["side_effect"]]
    
    #Creating Hyperedges
    # create hyper edge between drugs and hypernodes
    # Convert the string representation of lists back to actual lists
    polypharmacy_grouped["drug_combination"] = polypharmacy_grouped["drug_combination"].str.split("|")

    # create hyperedge
    graph["drugs", "hyperedge_part_1", "hypernodes"].edge_index = torch.cat(
        (torch.from_numpy(np.array(polypharmacy_grouped["drug_combination"].explode().astype(float).astype(np.int64), dtype=np.int64)), 
         torch.tensor(polypharmacy_grouped["drug_combination"].explode().index)
         )
    ).reshape(-1, len(polypharmacy_grouped["drug_combination"].explode())
    ).to(torch.int64)

    graph["hypernodes", "hyperedge_part_2", "drugs"].edge_index = torch.cat(
        (torch.tensor(polypharmacy_grouped["drug_combination"].explode().index), 
        torch.from_numpy(np.array(polypharmacy_grouped["drug_combination"].explode().astype(float).astype(np.int64), dtype=np.int64))
        )
    ).reshape(-1, len(polypharmacy_grouped["drug_combination"].explode())
    ).to(torch.int64)
    
    # store the graph
    GRAPH_PATH = os.path.join(path, "graph.pk")
    with open(GRAPH_PATH, "wb") as f:
        pk.dump(graph, f)

    print("Graph Create Done!")
    return graph

```


## Model Architecture

The model architecture, named SEPIA (Side Effect Prediction with Interaction Awareness), is designed for drug interaction and side effect prediction, leveraging the graph representation of polypharmacy data. The model consists of an Encoder and a Decoder.

```python title="sepia"
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

### Encoder:
* **Input**: \
Graph representation of the biological data, including drugs, proteins, and their interactions, along with identified side effects. 

* **Output**: \
Embeddings representing the interactions and effects. 

* **Architecture**: \
Consists of SAGEConv instances for processing heterogeneous graph data, and an embedding layer for side effects.

``` python title="encoder"
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

```python title="decoder"
class Decoder(nn.Module):
    def __init__(self, emb_dim):
        super(Decoder, self).__init__()
        self.Sigmoid = nn.Sigmoid()
        self.Linear = nn.Linear(emb_dim, 1)

    def forward(self, embs):
        embs = torch.stack([torch.prod(x, dim=0) for x in embs])
        return self.Sigmoid(self.Linear(embs))
```


### Negative Sampler:

* **Input**: \
Graph, Batch size, and number of side effects we want to generate.

* **Output**: \
Random generated side effects.

* **Functionality**: \
Generate negative samples (Random Side effects) for training the SEPIA model.

```python title="negative sampler"

def hyperedge_size_distribution(graph):
    out_edges = graph.edge_index_dict[('hypernodes', 'hyperedge_part_2', 'drugs')][0]
    counts = torch.bincount(torch.bincount(out_edges))
    fractions = counts / sum(counts)
    distribution = {
        i: float(fractions[i]) for i in range(len(fractions))
    }
    return distribution

def random_neg_sample(graph, batch_size, n_effects):
    distribution = hyperedge_size_distribution(graph)
    num_nodes = np.random.choice(list(distribution.keys()), p=list(distribution.values()))
    nodes = [torch.tensor(np.random.choice(len(graph["drugs"].x), size=num_nodes,replace=False)) for _ in range(batch_size)]

    effects = [torch.tensor(np.random.choice(n_effects)) for _ in range(batch_size)]
    
    return nodes, effects
```


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
Backpropagation: Gradients are calculated and the model’s parameters are updated using an optimizer.

**5. Testing**: \
The model is evaluated on the test data, where it predicts side effects for given interactions.
Metrics Calculation: Calculates metrics like ROC AUC to evaluate the model's performance.

**6. Visualization**: \
Plot the ROC curve for both training and testing data to visualize the model’s performance, and store the confusion matrix for the testing set.

```python title="train"
# Training Loop
for epoch in range(1):
    train_loss_sepia = 0
    train_preds = torch.tensor([])
    train_labels = torch.tensor([])
    i = 0
    for pos_mask, pos_nodes, pos_effect_ids, hypernode_ids in tqdm(train_loader, desc="Training: "):
        model.train()
        sepia_optimiser.zero_grad()

        neg_nodes, neg_effect_ids = random_neg_sample(train_graph, batch_size, len(train_graph["hypernodes"].x[0]))
        neg_mask = k_hop_graph(n_hops, "drugs", torch.cat(neg_nodes).unique(), train_graph.edge_index_dict, train_graph, drop_fraction)
        mask = { key: torch.cat((pos_mask.get(key,torch.tensor([], dtype=torch.int64)), neg_mask.get(key,torch.tensor([], dtype=torch.int64)))).unique() for key in set(pos_mask.keys()) | set(neg_mask.keys()) }
        
        #Remove hypernodes that should be predicted
        mask['hypernodes'] = mask['hypernodes'][~torch.isin(mask['hypernodes'], hypernode_ids)]
        
        pos_nodes = [torch.tensor([(mask['drugs'] == y).nonzero().flatten() for y in x]) for x in pos_nodes]
        neg_nodes = [torch.tensor([(mask['drugs'] == y).nonzero().flatten() for y in x]) for x in neg_nodes]

        subgraph = train_graph

        pos_preds = model(subgraph, pos_nodes, pos_effect_ids)
        neg_preds = model(subgraph, neg_nodes, neg_effect_ids)
        preds = torch.cat((pos_preds, neg_preds))

        labels = torch.cat((
            torch.ones(len(pos_nodes)),
            torch.zeros(len(neg_nodes))
        ))

        loss_sepia = torch.nn.functional.binary_cross_entropy(preds.squeeze(), labels)
        loss_sampler = negative_sampler_loss(neg_preds)

        loss_sepia.backward(retain_graph=True)

        sepia_optimiser.step()

        train_loss_sepia += loss_sepia.detach()
        train_preds = torch.cat((train_preds, preds.detach()))
        train_labels = torch.cat((train_labels, labels.detach()))

        if i % 100 == 0:
            sum_test_loss_sepia = 0
            test_preds = torch.tensor([])
            test_labels = torch.tensor([])

            model.eval()
            with torch.no_grad():
                for pos_mask, pos_nodes, pos_effect_ids, hypernodes in test_loader:
                    neg_nodes, neg_effect_ids = random_neg_sample(test_graph, batch_size, len(test_graph["hypernodes"].x[0]))

                    neg_mask = k_hop_graph(n_hops, "drugs", torch.cat(neg_nodes).unique(), test_graph.edge_index_dict, test_graph)

                    mask = { key: torch.cat((pos_mask.get(key,torch.tensor([], dtype=torch.int64)), neg_mask.get(key,torch.tensor([], dtype=torch.int64)))).unique() for key in set(pos_mask.keys()) | set(neg_mask.keys()) }
                    pos_nodes = [torch.tensor([(mask['drugs'] == y).nonzero().flatten() for y in x]) for x in pos_nodes]
                    neg_nodes = [torch.tensor([(mask['drugs'] == y).nonzero().flatten() for y in x]) for x in neg_nodes]

                    mask['hypernodes'] = mask['hypernodes'][~torch.isin(mask['hypernodes'], hypernode_ids)]

                    subgraph = test_graph

                    labels = torch.cat((
                        torch.ones(len(pos_nodes)),
                        torch.zeros(len(neg_nodes))
                    ))

                    pos_preds = model(subgraph, pos_nodes, pos_effect_ids)
                    neg_preds = model(subgraph, neg_nodes, neg_effect_ids)
                    preds = torch.cat((pos_preds, neg_preds))
                    
                    test_loss_sepia = torch.nn.functional.binary_cross_entropy(preds.squeeze(), labels)

                    sum_test_loss_sepia += loss_sepia.detach()
                    test_preds = torch.cat((test_preds, preds.detach()))
                    test_labels = torch.cat((test_labels, labels.detach()))

            fpr, tpr, _ = roc_curve(test_labels.detach(), test_preds.detach())
            plt.plot(fpr,tpr, label="test")
            fpr, tpr, _ = roc_curve(train_labels.detach(), train_preds.detach())
            plt.plot(fpr,tpr, label="train")

            plt.legend(loc="lower right")

            plt.savefig(f"roc/{epoch}-{i}.png")
            plt.clf()

            # Compute binary predictions and confusion matrix
            binary_preds = (test_preds.detach() > 0.5).float() * 1
            tn, fp, fn, tp = confusion_matrix(test_labels.detach(), binary_preds).ravel()

            # Store the results in a dictionary
            results = {
                'Epoch': epoch,
                'Batch': i,
                'True Positives': tp,
                'True Negatives': tn,
                'False Positives': fp,
                'False Negatives': fn,
            }

            # Append the results to the CSV file in real-time
            append_results_to_csv(filepath, results)

            tqdm.write(f"Epoch {epoch} - {i} | Train Loss: {round(float(train_loss_sepia)/len(train_loader), 3)}, Train AUC: {round(roc_auc_score(train_labels.detach(), train_preds.detach()),3)} | Test Loss: {round(float(sum_test_loss_sepia)/len(test_loader), 3)}, Test AUC: {round(roc_auc_score(test_labels.detach(), test_preds.detach()),3)}", end="\n")
            path = f"trained_model/model_{i}.pt"
            torch.save(model.state_dict(), path)
            train_preds = torch.tensor([])
            train_labels = torch.tensor([])
            train_loss = 0
        i+=1
```



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
| Accuracy        | 1       | 1      |
| Precision       | 1       | 1      |

### Confusion matrix 

#### Decagon Dataset

|    | TP | FP |
|----|----|----|
| TN | 1  | 2  |
| FN | 3  | 4  |

#### Nsides Dataset

|    | TP | FP |
|----|----|----|
| TN | 1  | 2  |
| FN | 3  | 4  |

## References

[^1]: Marinka Zitnik, Monica Agrawal, Jure Leskovec, Modeling polypharmacy side effects with graph convolutional networks, Bioinformatics, Volume 34, Issue 13, July 2018, Pages i457–i466, https://doi.org/10.1093/bioinformatics/bty294

[^2]: Vanguri, Rami; Romano, Joseph; Lorberbaum, Tal; Youn, Choonhan; Nwankwo, Victor; Tatonetti, Nicholas (2017). nSides: An interactive drug--side effect gateway. figshare. Dataset. https://doi.org/10.6084/m9.figshare.5483698.v2

[^3]: David Weininger. 1988. SMILES, a chemical language and information system. 1. introduction to methodology and encoding rules. J. Chem. Inf. Comput. Sci. 28, 1 (February 1988), 31–36. https://doi.org/10.1021/ci00057a005

[^4] Decagon dataset preprocessing. https://github.com/jbr-ai-labs/simvec/blob/main/data/data_preprocessing.ipynb 

[^5] STITCH databank. http://stitch.embl.de/

[^6] Molformer. https://github.com/IBM/molformer