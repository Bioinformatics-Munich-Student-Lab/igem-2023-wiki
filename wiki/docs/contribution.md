
# Contribution

## Introduction
Polypharmacy means taking a lot of different medications at the same time, which can happen when a person has several health conditions or sees multiple doctors. While these medications can help with specific problems, they can also lead to problems like interactions, side effects, or confusion. Polypharmacy is one of the pressing issues of today's healthcare systems. It is defined as the concurrent use of five drugs or more by a single patient. Across Europe, polypharmacy is highly prevalent, with a prevalence of 32.1% for persons of age 65+ [^1]. The SEPiA Team took action, developed a neuronal network that can predict these side effects to prevent polypharmacy, and developed the first polypharmacy model that can use multiple drugs as input. Sepia is an attempt to provide a solution which is easy to use for patients, medical personnel as well as future researchers. To make sure that Sepia is as easy to use as possible, we developed both a user-oriented interface and python packages for easy distribution. With its user interface, Sepia can be a significant benefit for patients and doctors looking for side effects with prescribed medication. For research and development with Sepia, we offer an easy-to-use python package on PyPI [^2].Pretrained models and a docker container will also be made available through the Sepia GitHub repository [^3]. In the following, you can read about what kind of trouble we run into and what else you have to keep in mind if you want to do similar tasks.

## Data handling 
Our first task was to find enough data to be able to properly train our model which also doesn’t take to many restrictions to work with these data. In the end we took data of the FDA which is already de-identified patient. One advantage of this decision was that we did have to pay for this data because it is for free available. When using these data you have to follow specific guidelines to pretect the patients.

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
We deploy our neural network in different ways. We deploy our model on our [Hugging Face account](https://huggingface.co/BioinformaticsMunichStudentLab), so people who may not be familiar with iGEM can benefit from our work and get in touch with our project. Another option is to download our code from our [GitLab](https://gitlab.igem.org/2023/software-tools/munichbioinformatics) and use our model as a foundational model, adjusting our code to your application. Instructions on how to work with our PyPi package are provided [hier](/munichbioinformatics/contribution/#how-to-use-the-pypi-package). To try our model without any coding skills, you can visit our website and test its accuracy. Instructions on how to use [our website](http://sepia.bmsl.org/) are outlined below.

## How to use our graphical user interface 
### The structure of our UI 
Our UI can be split into three parts: the search bar, the list of drugs, and the list of polypharmacy.
In the middle of the screen is our search bar, which can be used to search for and add a drug. This can be done multiple times to add multiple drugs. On the left side of the screen is the list of drugs, which displays every drug that has been added through the search bar. Each listed drug has a delete button to remove it from the calculation. On the right side are listed polypharmacies that are likely to occur because of the added drugs. Each polypharmacy has a displayed score, indicating how likely it is to occur.
### our vision how to use the model
Here is how we envision it should be used: For example, you are a doctor and want to determine how dangerous it is to give your patient four specific drugs at the same time. You can add each drug through the search bar, make any necessary adjustments in the list of drugs, and check the calculations on the right. Now, you may want to explore similar drugs that have the same effect as the other drugs but a lower probability of causing polypharmacy.
Now it's time to try our model yourself on [our website](http://sepia.bmsl.org/).

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

