# Software-engineering Success in SEPIA

Polypharmacy presents a complex and non-linear, but common risk profile.
It is also a highly intersectional issue, involving doctors, pharmacists, caregivers and pharma companies.
To identify how we as bioinformaticians could make a meaningful contribution to this multifacetted issue, we first extensively researched the existing literature and reached out to key subject-matter experts: Dr. Markus List, group leader at TUM and jointly responsible for the bioinformatics part of the REPO4EU project aiming to enable drug repurposing and Prof. Julia Stingl, head of the Clinical Pharmacology department at the University Hospital Aachen and one of Germany's leading researchers in polypharmacy.

To our surprise, we discovered that previous Bioinformatics approaches for predicting drug-drug interactions had solely focused on patients taking two drugs at once, whereas a typical patient in a care setting might on average take 5-10 drugs.
By discussing with stakeholders at an early stage, we were able to identify this issue and also learn that most of the drugs taken by a polypharmaceutic patient are not novel (think painkillers, diuretics, SSRIs) and fairly well-characterized.
After this step of requirements engineering, we decided to base our engineering project on a previous drug-drug interaction prediction pipeline (»Decagon«) using multimodal drug-protein and protein-protein interaction networks that excels at predicting the pairwise interactions between well-characterized drugs[0] – we could afford to use this robust architecture instead of more modern transformer-based approaches because we knew that a typical patient would be taking mostly well-characterized substances.

However, both the dataset used for training and the codebase of Decagon proved to be seriously outdated.
Instead of extending an six-year-old codebase and forever locking our project into `tensorflow 2.7`, we chose to create a new training dataset and reimplement Decagon as a first step.
For this, we split into sub-teams and used agile software development techniques, with weekly synchronization meetings to keep all parts of our projects working smoothly with each other.

Reimplementing Decagon took a significant amount of time, but by starting from a modern and lean codebase we had full knowledge of, we were able to quickly extend SEPIA to predict true polypharmacy.
For this, we first used a library implementing hyperedges


[0] <Decagon>
