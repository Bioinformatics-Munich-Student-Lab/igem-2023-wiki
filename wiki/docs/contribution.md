
# Contribution

## Introduction
Polypharmacy is one of the pressing issues of today's healthcare systems. It is defined as the concurrent use of five drugs or more by a single patient. Across Europe, polypharmacy is highly prevalent, with a prevalence of 32.1% for persons of age 65+[^1]. Most of the issues with polypharmacy stem from the fact that drug-drug interactions and adverse side effects (ADRs) are not known or not considered in healthcare decisions.

The SEPiA team took action. A novel graph-convolutional neural network that can predict polypharmacy side effects has been developed. To our knowledge, SEPiA is the first polypharmacy side effect model that can handle true polypharmacy, meaning that it is not limited to predict only side effects that are caused by pairs of drugs. SEPiA is an attempt to provide a solution which is easy to use for patients, medical personnel as well as future researchers. To ensure that SEPiA is as easy to use as possible, we developed both a user-oriented interface and python packages for easy distribution. For research and development with SEPiA, we offer an easy-to-use python package on PyPI[^2] as well as the source code, models and containers though the SEPiA git repository[^3].

## Data handling 
Training the SEPiA models requires data about polypharmacy side effects. Our first task was to find enough data to be able to properly train, test and validate the SEPiA model. We opted for the already de-identified, anonymized and freely available [nsides](https://tatonettilab.org/offsides/) dataset. This turned out to be a very good decision, as the dataset is large enough to be able to train the SEPiA model while also protecting the privacy of sensitive patient's data.

## Where to find Healtcare data
| Method      | Description                          |
| ----------- | ------------------------------------ |
| `Government Health Agencies`| National Institutes of Health Data Sharing Repositories (e.g., PubMed, GenBank) contain valuable medical and biological data.|
| `Academic Research Institutions`| Many universities and research institutions share medical datasets for research purposes. Stanford's MIMIC-III dataset for critical care research or the Cancer Genome Atlas (TCGA) for cancer-related research|
| `Open Data Initiatives`| Some organizations and initiatives focus on making medical data openly accessible. For instance, OpenMRS is an open-source medical record system that collects data from various healthcare settings |
| `Data Science Competitions`| Platforms like Kaggle host data science competitions that often include medical datasets |
| `Data Marketplaces`| marketplaces like IBM Watson Health's MarketScan, offer medical datasets for purchase or licensing |
| `Collaboration with Healthcare Providers`| hospitals, clinics, or healthcare institutions are able to provide de-identified patient data. To do this, you have to keep privacy regulations like HIPAA in the United States in mind|

## Deploying our model in different ways 
We deploy our neural network in different ways. We deploy our model on our [Hugging Face account](https://huggingface.co/BioinformaticsMunichStudentLab), so a pretrained checkpoint can be downloaded and other people who may not be familiar with iGEM can benefit from our work and get in touch with our project. Another option is to download our code from our [SEPiA Git repository ](https://gitlab.igem.org/2023/software-tools/munichbioinformatics) use SEPiA as a foundational model, adjusting the code to the specific application at hand. Instructions on how to work with our PyPi package are provided [hier](/munichbioinformatics/contribution/#how-to-use-the-pypi-package).Also, a basic pretrained checkpoint is included in the SEPiA PyPI repository. To try the SEPiA model without any coding or computationally expensive training, you can visit a live website and test its accuracy. Instructions on how to use [our website](http://sepia.bmsl.org/) are outlined below.

## How to use our graphical user interface 
### The structure of our UI 
Our UI can be split into three parts: the search bar, the list of drugs, and the list of polypharmacy.
In the middle of the screen is our search bar, which can be used to search for and add a drug. This can be done multiple times to add multiple drugs. On the left side of the screen is the list of drugs, which displays every drug that has been added through the search bar. Each listed drug has a delete button to remove it from the calculation. On the right side are listed polypharmacies that are likely to occur because of the added drugs. Each polypharmacy has a displayed score, indicating how likely it is to occur.

!!! example "UI Demo Prototype"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/ui-demo-1.jpeg){ width=800" }
    <figcaption>This is the initial prototype for the UI that healthcare professionals would use to interact with our model</figcaption>
    </figure>

### Future development
We envision a tight integration into existing and novel clinical software. Ideally, a patient management system which already contains the necessary information about patient's condition and medication could be enhanced with SEPiA. Medication could automatically be checked for problematic combinations, suggesting substitutions where applicable.

For patients, the website will be further improved by adding trivial or trade names to the list of drugs and the ability to search for medication by the indicating medical condition.
Now it's time to try our model yourself on [our website](http://sepia.bmsl.org/).


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

Further documentation can be found in our [Git repository](https://github.com/Bioinformatics-Munich-Student-Lab/sepia).

# BIOINFORMATICS MUNICH STUDENT LAB E.V.
We are proud of having established a non-profit organization for Bioinformatics students, a development that promises to simplify the process of initiating new student projects in the future. This non-profit organization will not only simplify the process of initiating projects but will also create opportunities for attracting sponsors in the future. German companies, for instance, can avail themselves of a tax reduction benefit by sponsoring a non-profit organization.

Our primary objective is to inspire students in the early stages of their careers to participate in competitions such as iGEM, thereby gaining invaluable experience, much like we did through our iGEM journey. By supporting these budding talents, we aim to foster a thriving community of young bioinformaticians who can contribute to the field's advancement and make a positive impact on the world of science and technology, and we hope that we can recruit more people next year to take part in the iGEM competition through our new non-profit organisation.
If you want to join the BIOINFORMATICS MUNICH STUDENT LAB E.V. or just want more information, [click here](https://bmsl.org/) to go to our website.

# how future iGEM teams can benefit from our project 
The groundwork we've established in our project offers benefits to other iGEM teams. Our efforts have created an opportunity for future teams to elevate the project to greater levels. Initially, they can capitalize on our pre-existing codebase and enhance our machine learning model. By expanding the dataset, incorporating more diverse sources of data, and delving into the integration of omics data, they can enhance the accuracy and versatility of the model. Instead of relying solely on data from the USA, teams can source information from different populations, including Europe, ensuring a more comprehensive and globally applicable approach to mitigating polypharmacy risks.

Moreover, for iGEM teams keen on developing healthcare applications, our project provides an invaluable head start. They can seamlessly integrate our machine learning model into their software projects, instantly incorporating a functional and vital feature. This not only expedites the development process but also ensures that their applications are equipped with the latest advancements in predicting drug interactions, potentially making a meaningful impact on patient safety and healthcare outcomes.

[^1]: https://doi.org/10.1016/j.archger.2018.06.018

[^2]: https://pypi.org/project/sepia-polypharmacy/

[^3]: https://github.com/Bioinformatics-Munich-Student-Lab/sepia

