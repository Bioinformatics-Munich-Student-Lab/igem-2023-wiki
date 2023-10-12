---
template: custom/contentpage.html
hero_text: Engineering
hero_image1: https://static.igem.wiki/teams/5016/wiki/engineering-1.jpg
hero_image2: https://static.igem.wiki/teams/5016/wiki/blur-2-left.webp
hero_image3: https://static.igem.wiki/teams/5016/wiki/blank.png
hero_image4: https://static.igem.wiki/teams/5016/wiki/blur-1-right.webp
---

# Software Engineering Success in SEPIA

Polypharmacy presents a complex and non-linear but highly prevalent risk profile [^1] [^2] [^3].\
It is also a highly intersectional issue involving doctors, pharmacists, biologists, caregivers, regulators, and pharma companies [^3] [^4].\
To identify how we, as bioinformaticians, could make a meaningful contribution to this multifaceted issue, we first extensively researched the existing literature and reached out to key subject-matter experts.

To our surprise, we discovered that previous Bioinformatics approaches for predicting drug-drug interactions had solely focused on patients taking two drugs at once, whereas a typical patient in a care setting might on average, take 5-10 drugs [^3] [^5].

We have outlined some of the more significant engineering cycles we completed.

## Agile Development

In order to tackle this problem, we adhered to the engineering design cycle, which is commonly found in synthetic biology but also in software engineering.\
We enhanced the engineering cycle using principles from Agile to increase productivity in a fast-paced software-focused development team.

Agile is a software development methodology and set of principles that emphasize flexibility, collaboration, and customer-centricity to deliver high-quality software efficiently.\
It is an iterative and incremental approach to software development that contrasts with traditional, linear methodologies.\
Agile methodologies promote adaptability, transparency, and constant improvement throughout the development process.

Agile encourages delivering working software at the end of each iteration.\
This ensures that the software is always in a potentially shippable state, which can be released to customers whenever necessary. As such, we were forced to repeatedly go through the engineering cycle.

We found the agile-inspired workflow to work well for the project.\
Due to our small team size, it was paramount that tasks were distributed and completed efficiently.\
Our implementation of the agile engineering cycle demanded two weekly meetings for the development teams. Team members were incentivized to discuss more specific issues in smaller meetings, where only those who were needed had to be present.\
We aimed to iterate through the engineering cycle once every two weeks (a sprint), meaning everybody had four opportunities to show their progress and receive feedback.\
During the project, we used a GitHub organization to maintain multiple Git repositories for different subprojects and track issues and deliverables during each sprint.

On the one hand, we were able to dive deeply into the code and work on implementing novel machine learning techniques, but on the other hand, the regular check-ins with other team members and collaborators grounded us to keep a view on the real-world problem we were working on.

<figure markdown>
  ![Image title](https://static.igem.wiki/teams/5016/wiki/engineering-001.jpeg){ width="1800" }
  <figcaption>The adaptation of the engineering cycle for machine learning development that we adhered to for the course of our project</figcaption>
</figure>

## The design cycle in machine learning development

Building an AI model involves a structured process consisting of four key steps: design, build, test, and learn.

### Design

The first step is clearly defining the problem you want the AI model to solve.\
Understand the problem domain, the specific objectives, and the expected outcomes.\
This often involves consulting with domain experts and stakeholders to ensure a deep understanding of the problem.

Identify and collect the data necessary for training and testing the model.\
Data must be cleaned, preprocessed, and prepared in a format suitable for machine learning.\
Consider issues like data quality, missing values, and data imbalance.

Define the structure of the AI model, including the number of layers, neurons, and activation functions in neural networks or the choice of algorithms and parameters for other machine learning models.

Decide on appropriate evaluation metrics that will measure the model's performance.\
This may include metrics like accuracy, precision, recall, F1-score, or mean squared error, depending on the problem type.

### Build

Divide the data into training, validation, and testing sets.\
The training data is used to train the model, the validation data helps tune hyperparameters, and the testing data is used to assess the model's generalization.

Train the AI model using the training dataset and fine-tune hyperparameters to optimize performance.\
This step often involves iterations and experimenting with different settings.

Implement regularization techniques and other strategies to prevent overfitting and improve the model's generalization to unseen data.

Implement the model using appropriate programming languages and libraries, such as Python and TensorFlow or PyTorch, for deep learning.

### Test

Evaluate the model's performance on the validation and testing datasets using the chosen evaluation metrics.\
Assess whether the model meets the desired criteria and can generalize to new data.

Analyze model errors to identify patterns and areas where the model struggles.\
This can lead to further improvements in the design and build stages.

### Learn

Iterate and Refine: Based on the results of testing, refine the model, adjust hyperparameters, and make design modifications as needed.\
Iterate through the build and test phases until the desired level of performance is achieved.

Document all processes, parameters, and findings for future reference.\
This documentation is valuable for sharing insights with stakeholders and for model maintenance.

If the model passes testing and meets the defined success criteria, it can be deployed for real-world applications.\
Monitor its performance in production and be prepared to make updates and improvements as needed.

This iterative process will require multiple iterations through the engineering cycles to develop a robust and effective AI model.\
Continuous learning and adaptation are essential in the field of AI and machine learning due to evolving data and changing requirements.

---

## Cycle I - Adapt Existing Work

We all stand on the shoulders of giants.\
A great way to gain some initial insights into a topic is by adapting something that already exists.

### Design I

After the initial step of careful requirements engineering and gaining an overview of previous work in this field, we decided to base our engineering project on a previous drug-drug interaction prediction pipeline, `Decagon`, using multimodal drug-protein and protein-protein interaction networks [^6].\
Decagon excels at predicting the pairwise interactions between well-characterized drugs, but its performance is limited for drugs that are not well characterized (and typically more novel or rarely prescribed).\
This is a tradeoff we felt comfortable making, as we knew that a typical patient would be taking mostly well-characterized substances.

!!! example "Decagon Architecture"
    <figure markdown>
    ![Decagon multimodal graph](https://static.igem.wiki/teams/5016/wiki/decagon.jpeg){ width="600"}
    <figcaption>The multimodal graph used by Decagon. Figure from Zitnik et al. 2018.</figcaption>
    </figure>

### Build I

Both the dataset used for training and the codebase of Decagon proved to be outdated regarding, due to being created in 2016.\
Instead of extending a six-year-old codebase and forever locking our project into `Tensorflow 2.7`, we chose to create a new training dataset from drug interactions and adverse events reported to the FDA.\
Consequently, reimplementing `Decagon` was our first deliverable.\
For this, we split into sub-teams and used agile software development techniques, with weekly synchronization meetings to keep all parts of our projects working smoothly with each other.\
Reimplementing Decagon using pytorch and a modernized version of the training dataset took us four sprints, but by starting from a modern and lean codebase we had full knowledge of, we were able to quickly extend our model to address the problem of true polypharmacy prediction.

### Test I

For this, we had to extend the graph used by Decagon to incorporate the possibility of multiple drugs interacting at once.\
In a simple graph, these kinds of relationships – more technically referred to as hyperedges – cannot be natively represented.\
Consequently, we were getting adequate results for pairwise predictions but had yet to fulfill our goal of enabling true polypharmacy predictions.

### Learn I

However, current Machine Learning frameworks are limited to these simple graph representations.\
We decided to take an alternative approach and find a way to encode the hyperedge information in a simple graph.\
We added another node type to the graph that represents multi-drug interactions.\
During graph construction, all interactions present in the training data are added as a node to the graph, and a connection to each of the drugs present in the interaction is added.\
The model then learns this graph structure, turning the multidrug interaction problem from a hyperedge prediction problem into a simple link prediction problem.

## Cycle II - Initial Build

### Design II

Based on what we were able to learn from the previous cycle, we decided to rebuild the entire architecture.

!!! example "Mapping out data structures and model architecture"
    <figure markdown>
    ![Image title](https://static.igem.wiki/teams/5016/wiki/model-design.jpg){ width="1800" }
    <figcaption>An adaptation of the engineering cycle for machine learning development that we adhered to for the course of our pro</figcaption>
    </figure>

### Build II

We implemented our mode inl [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/index.html) using the [SAGEConv](https://arxiv.org/pdf/1706.02216.pdf) architecture.\
PyTorch Geometric is a popular open-source library built on top of PyTorch, specifically designed for dealing with deep learning on graphs and irregular data.\
It provides a set of tools and utilities to make it easier to work with graph-based neural networks and apply them to a wide range of tasks, such as graph classification, node classification, and link prediction.

### Test II

For testing purposes and efficiency, we would use a subgraph for development purposes.\
This would lead to memory issues later on.
We used the AUC curve as our primary method of assessing performance.

The AUC is the area under the ROC curve.\
It quantifies the overall performance of the classification model.\
A perfect classifier has an AUC of 1, indicating that it can perfectly distinguish between the two classes.\
A random classifier has an AUC of 0.5, corresponding to the diagonal line from (0,0) to (1,1) in the ROC space.\
Typically, the higher the AUC, the better the model's ability to discriminate between the classes.

### Learn II

We found that the full training graph constructed to train the model would incorporate all of the information required but would crash during the training process because it was using more memory than our computers had available.

## Cycle III - Rebuild

### Design III

The initial model employed a single hypernode for each drug-effect combination, storing the effect type as a one-hot encoded vector within the node.\
However, this approach would have demanded a massive 4 terabytes of memory, rendering it impractical.\
The hourly cost of renting a machine that could manage this workload is greater than 100 USD.

### Build III

The solution was to aggregate all effects associated with a specific drug combination into a single hypernode and then extract individual effects during the training process.\
This strategy was effective with the pairwise Decagon/SimVec dataset.

Nonetheless, when dealing with the NSIDES dataset, it necessitated more than 64GB of memory.
To overcome this challenge, a further solution was implemented, which involved storing hypernode effect types as sparse tensors. This optimization substantially reduced memory usage.

### Test III

With these enhancements, the model became more memory-efficient, and it could be successfully trained on a standard laptop equipped with just 16GB of memory.\
We were able to witness an increase in the quality of predictions.

### Learn III

We observed that our neural net was learning much faster in the later training iterations than in the earlier iterations.\

!!! example "Drastic Performance Increase"
    <figure markdown>
    ![Image title](https://static.igem.wiki/teams/5016/wiki/perf-0-60.png){ width="600" }
    <figcaption>First Iteration</figcaption>
    </figure>
    <figure markdown>
    ![Image title](https://static.igem.wiki/teams/5016/wiki/perf-0-70.png){ width="600" }
    <figcaption>Second Iteration</figcaption>
    </figure>
    <figure markdown>
    ![Image title](https://static.igem.wiki/teams/5016/wiki/perf-0-230.png){ width="600" }
    <figcaption>Third Iteration</figcaption>
    </figure>

After iterating through the cycle many more times, we arrived at an architecture and a set of training parameters that yielded adequate performance.

[^1]: Van Wilder L, Devleesschauwer B, Clays E, Pype P, Vandepitte S, De Smedt D. Polypharmacy and Health-Related Quality of Life/Psychological Distress Among Patients With Chronic Disease. Prev Chronic Dis 2022;19:220062. DOI: [http://dx.doi.org/10.5888/pcd19.220062](http://dx.doi.org/10.5888/pcd19.220062)
[^2]: Masnoon N, Shakib S, Kalisch-Ellett L, Caughey GE. What is polypharmacy? A systematic review of definitions. BMC Geriatr. 2017 Oct 10;17(1):230. doi: 10.1186/s12877-017-0621-2. PMID: 29017448; PMCID: PMC5635569.
[^3]: Zhang N, Sundquist J, Sundquist K and Ji J (2020) An Increasing Trend in the Prevalence of Polypharmacy in Sweden: A Nationwide Register-Based Study. Front. Pharmacol. 11:326. doi: 10.3389/fphar.2020.00326
[^4]: Kantor ED, Rehm CD, Haas JS, Chan AT, Giovannucci EL. Trends in Prescription Drug Use Among Adults in the United States From 1999-2012. JAMA. 2015;314(17):1818–1830. doi:10.1001/jama.2015.13766
[^5]: Han K, Cao P, Wang Y, Xie F, Ma J, Yu M, Wang J, Xu Y, Zhang Y and Wan J (2022) A Review of Approaches for Predicting Drug–Drug Interactions Based on Machine Learning. Front. Pharmacol. 12:814858. doi: 10.3389/fphar.2021.814858
[^6]: Marinka Zitnik, Monica Agrawal, Jure Leskovec, Modeling polypharmacy side effects with graph convolutional networks, Bioinformatics, Volume 34, Issue 13, July 2018, Pages i457–i466, [https://doi.org/10.1093/bioinformatics/bty294](https://doi.org/10.1093/bioinformatics/bty294)
[^7]: Lukas Gosch, Simon Geisler, Daniel Sturm, Bertrand Charpentier, Daniel Zügner, Stephan Günnemann, arXiv:2306.15427 [cs.LG]
[^8]: Lukashina, N., Kartysheva, E., Spjuth, O. et al. SimVec: predicting polypharmacy side effects for new drugs. J Cheminform 14, 49 (2022). [https://doi.org/10.1186/s13321-022-00632-5](https://doi.org/10.1186/s13321-022-00632-5)
