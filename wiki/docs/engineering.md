# Software-engineering Success in SEPIA

Polypharmacy presents a complex and non-linear, but highly prevalent risk profile.
It is also a highly intersectional issue, involving doctors, pharmacists, caregivers, health agencies and pharma companies.
To identify how we as bioinformaticians could make a meaningful contribution to this multifacetted issue, we first extensively researched the existing literature and reached out to key subject-matter experts: Dr. Markus List, group leader at TUM and jointly responsible for the bioinformatics part of the REPO4EU project aiming to enable drug repurposing and Prof. Julia Stingl, head of the Clinical Pharmacology department at the University Hospital Aachen and one of Germany's leading researchers in polypharmacy.

To our surprise, we discovered that previous Bioinformatics approaches for predicting drug-drug interactions had solely focused on patients taking two drugs at once, whereas a typical patient in a care setting might on average take 5-10 drugs.
By discussing with stakeholders at an early stage, we were able to identify this issue and also learn that most of the drugs taken by a polypharmaceutic patient are not novel (think painkillers, diuretics, SSRIs) and fairly well-characterized.
After this step of requirements engineering, we decided to base our engineering project on a previous drug-drug interaction prediction pipeline (»Decagon«) using multimodal drug-protein and protein-protein interaction networks that excels at predicting the pairwise interactions between well-characterized drugs(0) – we could afford to use this robust architecture instead of a transformer-based approaches because we knew that a typical patient would be taking mostly well-characterized substances.

However, both the dataset used for training and the codebase of Decagon proved to be seriously outdated.
Instead of extending an six-year-old codebase and forever locking our project into `tensorflow 2.7`, we chose to create a new training dataset and reimplement Decagon as our first deliverable.
For this, we split into sub-teams and used agile software development techniques, with weekly synchronization meetings to keep all parts of our projects working smoothly with each other.

Reimplementing Decagon using `pytorch` and a modernized version of the training dataset took a significant amount of time, but by starting from a modern and lean codebase we had full knowledge of, we were able to quickly extend our codebase to predict true polypharmacy.

For this, we had to extend the graph used by Decagon to incorporate the possibility of multiple drugs interacting at once.
In a simple graph, these kinds of relationships – more technically referred to as hyperedges – cannot be natively represented.
However, current Machine Learning techniques only work on these kinds of simple graphs.
To address this, we instead added another node type to the graph, representing multi-drug interactions.
Each of these nodes is connected to all of the drugs in the interaction by an individual edge.
After implementing this in another sprint, we found that the graph constructed to train the model would incorporate all of the information required, but crash during the training process because it was using more memory than our computers had.

So we focused our next sprint on optimizing the model, reducing memory utilization by deduplicating the graph before training and streamlining the training process.
After this optimization, we were able to remove our earlier stop-gap solution of pruning the graph to contain only a subset of the full information and train once again on the full graph.

Meanwhile we also started working on deploying our model.
During requirements engineering, we had learned that in order to have a real-world impact in the clinic, our model would need to be easily usable by clinicians, without installing and training their own Machine Learning model or relying on external bioinformaticians to run predictions.
As the drugs a patient takes are not personally identifying medical information and can be freely processed, we decided to build a webserver that a physician or pharmacist can input a given medication plan into and receive predicted interactions among the prescribed drugs.
The physician can then identify potentially relevant interactions and adjust the medication plan or inform the patient, to empower pharmacovigilance in the clinic.

As we observed that our neural net was learning much faster in the later training iterations than in the earlier iterations, we tried in the next sprint training an adversarial network along our main network to generate sets of drugs that do *not* interact.
This is simpler to predict, and training the main model to discriminate these fake interactions from real interactions has been shown to improve training performance, particularly in graphs.
However, we observed that the adversarial network was getting too good a bit too fast, and narrowing down towards a set of clearly non-interacting drugs, causing training performance to decline sharply as training progressed, and overall increasing training time.

During the project, we used a GitHub organization to maintain multiple git repositories for different projects and track issues and deliverables for each sprint.
Communication in the team was handled asynchronously via slack, with a weekly virtual team meeting to make sure that when we were split up in small subteams we were still considering the big picture our subgoals fit into.

This flexible agile-inspired workflow we found to work well for the project.
On the one hand we were able to dive deeply into the code and work on implementing novel Machine Learning techniques, but on the other hand the regular check-ins with other team members and collaborators grounded us to keep a view on the real-world problem we were working on.



(0) <Decagon>
