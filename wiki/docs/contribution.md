
# Contributin

### Introduction
Polypharmacy means taking a lot of different medications at the same time, which can happen when a person has several health conditions or sees multiple doctors. While these medications can help with specific problems, they can also lead to problems like interactions, side effects, or confusion. Polypharmacy is one of the pressing issues of today's healthcare systems. It is defined as the concurrent use of five drugs or more by a single patient. Across Europe, polypharmacy is highly prevalent, with a prevalence of 32.1% for persons of age 65+ [^1]. The SEPiA Team took action, developed a neuronal network that can predict these side effects to prevent polypharmacy, and developed the first polypharmacy model that can use multiple drugs as input. Sepia is an attempt to provide a solution which is easy to use for patients, medical personnel as well as future researchers. To make sure that Sepia is as easy to use as possible, we developed both a user-oriented interface and python packages for easy distribution. With its user interface, Sepia can be a significant benefit for patients and doctors looking for side effects with prescribed medication. For research and development with Sepia, we offer an easy-to-use python package on PyPI [^2].Pretrained models and a docker container will also be made available through the Sepia GitHub repository [^3]. In the following, you can read about what kind of trouble we run into and what else you have to keep in mind if you want to do similar tasks.

### Data handling 
Our first task was to find enough data to be able to properly train our model which also doesn’t take to many restrictions to work with these data. In the end we took data of the FDA which is already de-identified patient. One advantage of this decision was that we did have to pay for this data because it is for free available. When using these data you have to follow specific guidelines to pretect the patients.

#### Where to find Healtcare data
| Method      | Description                          |
| ----------- | ------------------------------------ |
| `Government Health Agencies`| National Institutes of Health Data Sharing Repositories (e.g., PubMed, GenBank) contain valuable medical and biological data.|
| `Academic Research Institutions`| Many universities and research institutions share medical datasets for research purposes. Stanford's MIMIC-III dataset for critical care research or the Cancer Genome Atlas (TCGA) for cancer-related research|
| `Open Data Initiatives`| Some organizations and initiatives focus on making medical data openly accessible. For instance, OpenMRS is an open-source medical record system that collects data from various healthcare settings |
| `Data Science Competitions`| Platforms like Kaggle host data science competitions that often include medical datasets |
| `Data Marketplaces`| marketplaces like IBM Watson Health's MarketScan, offer medical datasets for purchase or licensing |
| `Collaboration with Healthcare Providers`| hospitals, clinics, or healthcare institutions are able to provide de-identified patient data. To do this, you have to keep privacy regulations like HIPAA in the United States in mind|


## How to use our graphical user interface 
#### The structure of our UI 
Our UI can be split into three parts: the search bar, the list of drugs, and the list of polypharmacy.
In the middle of the screen is our search bar, which can be used to search for and add a drug. This can be done multiple times to add multiple drugs. On the left side of the screen is the list of drugs, which displays every drug that has been added through the search bar. Each listed drug has a delete button to remove it from the calculation. On the right side are listed polypharmacies that are likely to occur because of the added drugs. Each polypharmacy has a displayed score, indicating how likely it is to occur.
#### our vision to use the model
Here is how we envision it should be used: For example, you are a doctor and want to determine how dangerous it is to give your patient four specific drugs at the same time. You can add each drug through the search bar, make any necessary adjustments in the list of drugs, and check the calculations on the right. Now, you may want to explore similar drugs that have the same effect as the other drugs but a lower probability of causing polypharmacy.

!!! example "UI Demo Prototype"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/ui-demo-1.jpeg){ width=800" }
    <figcaption>This is the initial prototype for the UI that healthcare professionals would use to interact with our model</figcaption>
    </figure>

## How to use the PyPI package
1. Install the `sepia-polypharmacy` package from PyPI.
    ```shell
    pip install sepia-polypharmacy
    ```

2. Train the model using your own polypharmacy datasets
    
    ```shell
    sepia train --train <training_set.csv> --test <test_set.csv> --checkpoint <path_to_model>
    ```
   
    OR

    Download a checkpoint file from a pretrained model.
    Checkpoint files will be made available. A default checkpoint file is also included in the PyPI version.


3. Use the trained model to predict side effects for your chemical compound of interest. The `--checkpoint` parameter can be omitted - the default model will then be used.

   ```shell
   sepia predict --checkpoint <path_to_model> --drugs <drug1> <drug2>
   ```

Further documentation can be found in our git repository [^3].


[^1]: https://doi.org/10.1016/j.archger.2018.06.018

[^2]: https://pypi.org/project/sepia-polypharmacy/

[^3]: https://github.com/Bioinformatics-Munich-Student-Lab/sepia

