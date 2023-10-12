# Software-engineering Success in SEPIA

Polypharmacy presents a complex and non-linear, but highly prevalent risk profile (Kantor et al. 2015; Zhang et al. 2020; van Wilder et al 2022).
It is also a highly intersectional issue, involving doctors, pharmacists, caregivers, regulators and pharma companies (Masnoon et al. 2017; van Wilder et al 2022).
To identify how we as bioinformaticians could make a meaningful contribution to this multifaceted issue, we first extensively researched the existing literature and reached out to key subject-matter experts:
Dr. Markus List, group leader at TUM and jointly responsible for the bioinformatics part of the [REPO4EU](https://repo4.eu/the-platform/) project developing methods for drug repurposing and Prof. Julia Stingl, head of the Clinical Pharmacology department at the University Hospital Aachen and one of Germany's leading researchers on polypharmacy and pharmacogenomics.


To our surprise, we discovered that previous Bioinformatics approaches for predicting drug-drug interactions had solely focused on patients taking two drugs at once, whereas a typical patient in a care setting might on average take 5-10 drugs (Kantor et al 2015; Zhang et al 2020).
By discussing with stakeholders at an early stage, we were able to identify this critical issue in the prior work and learn that most of the drugs taken by any given polypharmaceutic patient are old, widely available as generics and well-characterized (think NSAIDs, diuretics, SSRIs, statins).
After this step of requirements engineering and gaining an overview of previous work in this field, we decided to base our engineering project on a previous drug-drug interaction prediction pipeline (»Decagon«) using multimodal drug-protein and protein-protein interaction networks (Zitnik et al. 2018).
Decagon excels at predicting the pairwise interactions between well-characterized drugs, but its performance is limited for drugs that are not well characterized (and typically more novel or rarely prescribed).
This is a tradeoff we felt comfortable making, as we knew that a typical patient would be taking mostly well-characterized substances.


<figure markdown >
    ![Decagon multimodal graph](https://static.igem.wiki/teams/5016/wiki/decagon.jpg){ width="600"}
<figcaption>The multimodal graph used by Decagon. Figure from Zitnik et al. 2018.</figcaption>
</figure>


However, both the dataset used for training and the codebase of Decagon proved to be seriously outdated.
Instead of extending an six-year-old codebase and forever locking our project into `tensorflow 2.7`, we chose to create a new training dataset from drug interaction adverse events reported to the FDA, and reimplement Decagon as our first deliverable.
For this, we split into sub-teams and used agile software development techniques, with weekly synchronization meetings to keep all parts of our projects working smoothly with each other.

Reimplementing Decagon using `pytorch` and a modernized version of the training dataset took us almost two months, but by starting from a modern and lean codebase we had full knowledge of, we were able to quickly extend our model to address the problem of true polypharmacy prediction.

For this, we had to extend the graph used by Decagon to incorporate the possibility of multiple drugs interacting at once.
In a simple graph, these kinds of relationships – more technically referred to as hyperedges – cannot be natively represented.
However, current Machine Learning frameworks are limited to these simple graph representations.
So we decided to take an alternative approach, and find a way to encode the hyperedge information in a simple graph.
We added another node type to the graph that represents multi-drug interactions.
During the graph construction, all interactions present in the training data are added as a node to the graph, and a connection to each of the drugs present in the interaction is added.
The model then learns this graph structure, turning the multidrug interaction problem from a hyperedge prediction problem into a simple link prediction problem.

<figure markdown >
    ![Decagon multimodal graph](https://static.igem.wiki/teams/5016/wiki/hypergraph.jpg){ width="600"}
<figcaption>Our approach to encode true polypharmacy interactions in a simple graph model.</figcaption>
</figure>

After implementing this in our second sprint, we found that the graph constructed to train the model would incorporate all of the information required, but crash during the training process because it was using more memory than our computers had.
So we focused our next sprint on optimizing the model, reducing memory utilization by deduplicating the graph before training and streamlining the training process.
After this optimization, we were able to remove our earlier stop-gap solution of pruning the graph to contain only a subset of the full information and train once again on the full graph.

Meanwhile we also started working on deploying our model.
During requirements engineering, we had learned that in order to have a real-world impact in the clinic, our model would need to be easily usable by clinicians, without installing and training their own Machine Learning model or relying on external bioinformaticians to run predictions.
As the drugs a patient takes are not personally identifying medical information and can be freely processed, we decided to build a webserver that a physician or pharmacist can input a given medication plan into and receive predicted interactions among the prescribed drugs.
The physician can then identify potentially relevant interactions and adjust the medication plan or inform the patient, to empower pharmacovigilance in the clinic.

As we observed that our neural net was learning much faster in the later training iterations than in the earlier iterations, we tried in the next sprint training an adversarial network along with our main network to generate sets of drugs that do *not* interact.
This is simpler to predict, and training the main model to discriminate these fake interactions from real interactions has been shown to improve training performance, particularly in graph neural networks (Gosch et al, 2023).
However, we observed that the adversarial network was getting too good a bit too fast, and narrowing down towards a set of clearly non-interacting drugs, causing training performance to decline sharply as training progressed, and decreasing training performance overall.

To address the limitation of the base Decagon model of performance declining for drugs that are not well characterized, we decided to extend our graph once more, with edges between all drugs that are chemically similar to each other.
This allows the network to use the biochemical information of structurally similar compounds that may be better characterized, and further increased total model performance.
The advantages of this approach have been demonstrated in a recent pairwise drug interaction prediction software (Lukashina et al, 2022).

During the project, we used a GitHub organization to maintain multiple git repositories for different projects and track issues and deliverables for each sprint.
Communication in the team was handled asynchronously via slack, with a weekly virtual team meeting to make sure that when we were split up in small subteams we were still considering the big picture our subgoals fit into.

This flexible agile-inspired workflow we found to work well for the project.
On the one hand we were able to dive deeply into the code and work on implementing novel Machine Learning techniques, but on the other hand the regular check-ins with other team members and collaborators grounded us to keep a view on the real-world problem we were working on.


## References

Van Wilder L, Devleesschauwer B, Clays E, Pype P, Vandepitte S, De Smedt D. Polypharmacy and Health-Related Quality of Life/Psychological Distress Among Patients With Chronic Disease. Prev Chronic Dis 2022;19:220062. DOI: http://dx.doi.org/10.5888/pcd19.220062
Masnoon N, Shakib S, Kalisch-Ellett L, Caughey GE. What is polypharmacy? A systematic review of definitions. BMC Geriatr. 2017 Oct 10;17(1):230. doi: 10.1186/s12877-017-0621-2. PMID: 29017448; PMCID: PMC5635569.
Zhang N, Sundquist J, Sundquist K and Ji J (2020) An Increasing Trend in the Prevalence of Polypharmacy in Sweden: A Nationwide Register-Based Study. Front. Pharmacol. 11:326. doi: 10.3389/fphar.2020.00326
Kantor ED, Rehm CD, Haas JS, Chan AT, Giovannucci EL. Trends in Prescription Drug Use Among Adults in the United States From 1999-2012. JAMA. 2015;314(17):1818–1830. doi:10.1001/jama.2015.13766

Marinka Zitnik, Monica Agrawal, Jure Leskovec, Modeling polypharmacy side effects with graph convolutional networks, Bioinformatics, Volume 34, Issue 13, July 2018, Pages i457–i466, https://doi.org/10.1093/bioinformatics/bty294
Han K, Cao P, Wang Y, Xie F, Ma J, Yu M, Wang J, Xu Y, Zhang Y and Wan J (2022) A Review of Approaches for Predicting Drug–Drug Interactions Based on Machine Learning. Front. Pharmacol. 12:814858. doi: 10.3389/fphar.2021.814858
Lukas Gosch, Simon Geisler, Daniel Sturm, Bertrand Charpentier, Daniel Zügner, Stephan Günnemann, arXiv:2306.15427 [cs.LG]
Lukashina, N., Kartysheva, E., Spjuth, O. et al. SimVec: predicting polypharmacy side effects for new drugs. J Cheminform 14, 49 (2022). https://doi.org/10.1186/s13321-022-00632-5
