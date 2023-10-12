# Project Description

## Background
Polypharmacy refers to the simultaneous administration of multiple (>= 5) medications.\
While polypharmacy is a necessary part of treating multimorbid or vulnerable patients, it is associated with risk of adverse drug interactions, non-adherence and decline in quality of life.\
The risk profile of polypharmacy is non-linear and poorly understood.\
In care settings, polypharmacy can affect more than half of all patients; in total, about 15% of the USpopulation is considered to be polypharmaceutic – a rising trend in the context of an aging population.

Clinical or laboratory testing of every possible combination of drugs is infeasible.\
Computational prediction of polypharmacy side effects offers a much more scalable approach to reducing the risk associated with polypharmacy, however previous approaches have only predicted pairwise drug interactions.\
While predicting interactions between pairs of drugs is a much simpler problem from a Machine Learning perspective, this does not accurately model what we see in the clinic, with patients frequently taking 5-10 or more drugs simultaneously.\
This leads to current prediction models often showing very high performance in benchmarks, but failing when applied to clinical practice.

As the Munich Bioinformatics iGEM team, we identified this gap between Bioinformatics and the clinic and sought to tackle it.\
For this, we had meetings with many stakeholders, from the [REPO4EU](https://repo4.eu/) project and the university hospital Aachen to identify what exactly is the divergence between the bioinformatics state of the art and the clinical requirements.\
We also identified that a major focus of bioinformatics research – improving performance for novel or poorly characterized drugs – is mostly irrelevant from a clinical standpoint, as most patients would be taking old, well-characterized medications.\
For this reason, we chose to build SEPiA, a true polypharmacy prediction suite by starting from the base of Decagon, a previously published [^1] pairwise drug interaction prediction model.

SEPiAs approach is based on modelling the problem as a multimodal graph, and learning known biochemical and clinical interaction data.\
From this learned information, embeddings can be computed for each drug incorporating known drug-drug interactions, drug-protein and protein-protein interactions and its chemical structures.\
SEPIA then combines the embeddings using a set-transformer architecture to give a side effect prediction for a set of simultaneously administered drugs.\

Our team aims to make a significant impact both locally and globally with our project by predicting drug-drug interactions, and empowering clinicians, pharmacists and drug developers to improve pharmacovigilance and reduce adverse drug events.\
At the local level, we strive to improve healthcare outcomes within our community by providing healthcare professionals, starting with our collaboration partners at the university hospital Aachen, with a reliable and efficient tool to identify polypharmacy and prevent unwanted drug interactions.\
By working closely with stakeholders both inside and outside of the medical system (see Education), we hope to improve quality of medical care and extend the global healthspan.\
We also learned a lot from this project, both about managing a complex software project and about working with external collaborators and thinking critically about how we as Bioinformaticians can design software that addresses real issues in a way that it can be robustly deployed.


[^1]: Marinka Zitnik, Monica Agrawal, Jure Leskovec, Modeling polypharmacy side effects with graph convolutional networks, Bioinformatics, Volume 34, Issue 13, July 2018, Pages i457–i466, [https://doi.org/10.1093/bioinformatics/bty294](https://doi.org/10.1093/bioinformatics/bty294)
