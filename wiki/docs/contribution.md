# Contribution

### Introduction
Polypharmacy is one of the pressing issues of today's healthcare systems. It is defined as the concurrent use of five drugs or more by a single patient. Across Europe, polypharmacy is highly prevalent, with a prevalence of 32.1% for persons of age 65+[^1]. Most of the issues with polypharmacy stem from the fact that drug-drug interactions and adverse side effects (ADRs) are not known or not considered in healthcare decisions.

The SEPiA team took action. A novel graph-convolutional neural network that can predict polypharmacy side effects has been developed. To our knowledge, SEPiA is the first polypharmacy side effect model that can handle true polypharmacy, meaning that it is not limited to predict only side effects that are caused by pairs of drugs. SEPiA is an attempt to provide a solution which is easy to use for patients, medical personnel as well as future researchers. To ensure that SEPiA is as easy to use as possible, we developed both a user-oriented interface and python packages for easy distribution. For research and development with SEPiA, we offer an easy-to-use python package on PyPI[^2] as well as the source code, models and containers though the SEPiA git repository[^3].

# TODO which dataset do we use???
### Data handling
Training the SEPiA models requires data about polypharmacy side effects. Our first task was to find enough data to be able to properly train, test and validate the SEPiA model. We opted for the already de-identified, anonymized and freely available [nsides](https://tatonettilab.org/offsides/) dataset. This turned out to be a very good decision, as the dataset is large enough to be able to train the SEPiA model while also protecting the privacy of sensitive patient's data.

#### Where to find healthcare data
| Provider                                  | Description                                                                                                                                                                                                     |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Government Health Agencies`              | National Institutes of Health Data Sharing Repositories (e.g., PubMed, GenBank) contain valuable medical and biological data.                                                                                   |
| `Academic Research Institutions`          | Many universities and research institutions share medical datasets for research purposes. Stanford's MIMIC-III dataset for critical care research or the Cancer Genome Atlas (TCGA) for cancer-related research |
| `Open Data Initiatives`                   | Some organizations and initiatives focus on making medical data openly accessible. For instance, OpenMRS is an open-source medical record system that collects data from various healthcare settings            |
| `Data Science Competitions`               | Platforms like Kaggle host data science competitions that often include medical datasets                                                                                                                        |
| `Data Marketplaces`                       | marketplaces like IBM Watson Health's MarketScan, offer medical datasets for purchase or licensing                                                                                                              |
| `Collaboration with Healthcare Providers` | hospitals, clinics, or healthcare institutions are able to provide de-identified patient data. To do this, you have to keep privacy regulations like HIPAA in the United States in mind                         |

# Deploying the SEPiA model
To ensure that everyone can use the SEPiA model, we want to distribute it via a broad network of repositories and websites. In addition to the option to build and train a SEPiA model from scratch, a pretrained checkpoint can be downloaded from [Hugging Face](https://huggingface.co/BioinformaticsMunichStudentLab). Also, a basic pretrained checkpoint is included in the SEPiA PyPI repository.

Another option is to download the source code from the SEPiA git repository and use SEPiA as a foundational model, adjusting the code to the specific application at hand. To try the SEPiA model without any coding or computationally expensive training, you can visit a live website and test its accuracy. Instructions on how to use [the SEPiA website](http://sepia.bmsl.org/) are outlined below.

## How to use the SEPiA graphical user interface
### Website structure 
The SEPiA UI can be split into three parts: the search bar, the list of drugs, and the list of predicted side effects.
In the middle of the screen is the medication search bar, which can be used to search for and add a drug to the query. This can be done multiple times to add multiple drugs. On the left side of the screen is the list of drugs, which displays every drug that has been added through the search bar. Each listed drug has a delete button to remove it from the calculation. On the right side are predicted side effects that are likely to occur based on the medication. Each polypharmacy side effect has a displayed score, indicating how likely it is to occur.

!!! example "UI Demo Prototype"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/ui-demo-1.jpeg){ width=800" }
    <figcaption>This is the initial prototype for the UI that users would use to interact with the SEPiA model</figcaption>
    </figure>


### Future development
We envision a tight integration into existing and novel clinical software. Ideally, a patient management system which already contains the necessary information about patient's condition and medication could be enhanced with SEPiA. Medication could automatically be checked for problematic combinations, suggesting substitutions where applicable.

For patients, the website will be further improved by adding trivial or trade names to the list of drugs and the ability to search for medication by the indicating medical condition.

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

Further documentation can be found in the SEPiA git repository [^3].


[^1]: https://doi.org/10.1016/j.archger.2018.06.018

[^2]: https://pypi.org/project/sepia-polypharmacy/

[^3]: https://github.com/Bioinformatics-Munich-Student-Lab/sepia

