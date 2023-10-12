---
template: custom/contentpage.html
hero_text: Results
hero_image1: https://static.igem.wiki/teams/5016/wiki/results.jpg
hero_image2: https://static.igem.wiki/teams/5016/wiki/blur-4-left.webp
hero_image3: https://static.igem.wiki/teams/5016/wiki/blur-5-right.webp
hero_image4: https://static.igem.wiki/teams/5016/wiki/blank.png
---
Team Page

# SEPiA Results

Two machine learning models were developed to predict polypharmacy side effects. The first model was trained on pairwise drug data, similar to the approaches used by Decagon [^1] and SimVec[^2], and the second model utilized true polypharmacy data from NSIDES [^3], filtered to include only effects with at least 5000 total occurrences and drugs between 2 and 10.

## Training, Testing, and Validation Sets
The models were trained on 80% of the data, tested on 10%, and validated on another 10%. Using separate datasets for training, testing, and validation is crucial to ensure that the model is accurate, generalizable, and not overfitting to the training data. The testing set assesses the model's performance and tuning, while the validation set evaluates the model’s effectiveness on unseen data.

## Final Model Parameters
- **Optimizer**: AdamW optimizer was used to update the weights in the network to minimize the loss function. Optimizers are algorithms used to change the attributes of the neural network, such as weights and learning rate, to reduce the losses.

- **Learning Rate**: 0.001. The learning rate determines the size of steps that the optimizer takes while minimizing the loss function. A smaller learning rate may lead to a more precise convergence to the loss minimum, while a larger learning rate converges faster but may overshoot the minimum loss.

- **Batch Size**: The models were trained with a batch size of 2048. Batch size refers to the number of training examples utilized in one iteration. A smaller batch size often provides a regularizing effect and lower generalization error.

## Training Details
The models underwent training for 350 batches (pairwise data) and 600 batches (NSIDES data) respectively. The training was halted at these points as no consistent improvements were observed on the testing data.

## Model Output
The models outputs are values ranging from 0 to 1. An optimal cutoff for binary classification was determined via the ROC curve on the testing data, being 0.0676 for the pairwise model and 0.49 for the NSIDES model.

## Results
After finalising our modelling decisions, we applied our model to the respective validation sets. This allows us to get a final performance evaluation that is not biased by design decisions on the training or testing sets. 

### Performance Metrics
We used the following performance metrics to evaluate our model:

- **AUC**: Measures the area under the ROC curve, indicating the model’s ability to distinguish between classes. Higher AUC indicates better performance.

- **Sensitivity**: Measures the proportion of actual positives that are correctly identified. Important in identifying most of the potential side effects.

- **Specificity**: Measures the proportion of actual negatives that are correctly identified. Crucial for reducing false alarms.

- **ACC (Accuracy)**: Proportion of true results among the total number of cases examined.

- **F1 Score**: Harmonic mean of precision and recall, provides a balance between the two.

### Pairwise Results on Validation Set


!!! pairwiseroc "ROC Curve for pairwise model"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/pairwise-val-roc.svg){ width=600" }
        
    <figcaption>ROC curve for SEPiA model trained on the pairwise data also used by Decagon and SimVec. A random classifier would lie on the diagonal, while a perfect classifier would consist of streight lines going to 1.0. The closer the curve is to the 1.0, the better the classifier. The curve corresonds to a AUC of 0.895.</figcaption>
    </figure> 


<div class="grid cards" markdown>
- **Confusion matrix for binary predictions**
- **Performance metrics**


 |                              | Interaction     | No Interaction |
|------------------------------|:---------------:|:--------------:|
| **Predicted Interaction**    | 17665           | 5175           |
| **Prediction no interaction**| 2120            | 15305          |

| Metric           | Value     |
|------------------|:---------:|
| ROC AUC          | 0.895     | 
| Sensitivity      | 0.773     |
| Specificity      | 0.878     |
| ACC              | 0.819     |
| F1               | 0.829     |

</div>


The main performance metric used for link prediction tasks is the ROC curve and the associated AUC.
Our model performed on par with Decagon (AUC: 0.872) on pairwise data but worse than SimVec (AUC: 0.975). This shows, while we are competitive with state-of-the-art methods, that it may be possible to achieve further increases in performance by, for example, more carefully considering the way in which similarity between chemical structures is determined and utilized in the model.

When using the threshold determined on the test set, we archive an accuracy of 0.819 with a sensitivity about 0.1 higher than the specificity. This means that, at the optimal threshold for minimising both false positives and false negatives, our model is slightly better at identifying polypharmacy interaction but suffers from a higher rate of false positives.

!!! modelcomparison "Model Comparisons"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/method-comparison.svg){ width=600" }
        
    <figcaption>The bar plot shows the performance of Decagon, SimVec, and our SEPiA model trained on the pairwise data also used by the other two methods. SEPiA has a similar performance to Decagon, outperforming it slightly, while having a worse performance than SimVec.</figcaption>
    </figure>


### NSIDES Results on Validation Set
The main focus of our work was in extending polypharmacy prediction to multi-drug combinations. Thus the performance on the NSIDES dataset with between 2 and 10 drugs is essential.

!!! NSIDESroc "ROC Curve for NSIDES model"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/nsides-valid-roc.svg){ width=600" }
        
    <figcaption>ROC curve for SEPiA model trained on the NSIDES data for interactions of 2-10 drugs. The ROC curve is closer to 1.0 than the curve for the pairwise model. This shows that the predictions of the NSIDES SEPiA model are more reliable. The curve corresponds to an AUC of 0.982. </figcaption>
    </figure>


<div class="grid cards" markdown>
- **Confusion matrix for binary predictions**
- **Performance metrics**


 |                              | Interaction     | No Interaction |
|------------------------------|:----------------:|:--------------:|
| **Predicted Interaction**    | 332932            | 14236           |
| **Prediction no interaction**| 24369             | 344164          |

| Metric           | Value     |
|------------------|:---------:|
| ROC AUC          | 0.982     | 
| Sensitivity      | 0.96     |
| Specificity      | 0.934     |
| ACC              | 0.946     |
| F1               | 0.945     |

</div>

Here, we outperform the SEPiA model trained only on pairwise data. This might be due to a number of reasons. First, the much larger amount of training data might allow the model to learn more about the relations of drugs and polypharmacy effects. Also, the model learns from polypharmacy interactions resulting from different numbers of drugs. Thus, there may be structures hidden in the NSIDES data which are simply not available. 

This is especially noticeable when examining the performance stratified by the number of interacting drugs. Here the SEPiA model trained on NSIDES data reaches an AUC of 0.961 for pairwise interactions, an improvement of 0.066 when compared to the pairwise results of the SEPiA model only trained on the pairwise Decagon/SimVec dataset. In fact, this improvement makes our model competitive with the best-performing pairwise polypharmacy prediction tool SimVec.

It is also noticable how SEPiA performs better on interactions involving more drugs. The difference is especially noticable between 2 and 4 drugs, improving from 0.961 to 0.987. This may be due to a larger amount of information available from the graph for predicting interactions involving more drugs.

The binary predictions achieve an accuracy of 0.946 with a similar sensitivity (0.96) to specificity (0.934). This indicates that, overall, almost 95 of 100 predictions that the model makes are correct.  

!!! NSIDESroc "AUC of SEPiA stratified by number of drugs"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/auc-per-size.svg){ width=600" }
        
    <figcaption>The bar plot shows the performance of the SEPiA modelt trained on NSIDES data stratified by the number of drugs in the interaction. For easier visibility of the differences, the x-axis is set to 0.9. It is evident that the model performs better on interactions involving more drugs, with a decreasing difference between larger sets.</figcaption>
    </figure>
## Interpretation of Result

The SEPiA model shows promising results in predicting polypharmacy side effects, being competitive with state-of-the-art methods for pairwise predictions and extending current methodology to true polypharmacy. Its high AUC, sensitivity, and specificity suggest robust performance in both identifying true polypharmacy side effects and avoiding false alarms. These models can significantly aid in real-world applications, providing healthcare professionals and pharmacologists with valuable tools to anticipate and mitigate the adverse effects associated with polypharmacy, thereby enhancing patient safety and treatment efficacy.



## Reference
[^1]:  Decagon. Modeling polypharmacy side effects with graph convolutional networks
Marinka Zitnik, Monica Agrawal, Jure Leskovec https://arxiv.org/abs/1802.00543 

[^2]: Simvec. Lukashina, N., Kartysheva, E., Spjuth, O. et al. SimVec: predicting polypharmacy side effects for new drugs. J Cheminform 14, 49 (2022). https://doi.org/10.1186/s13321-022-00632-5

[^3]: nSides. Vanguri, Rami S et al. “nSides: An interactive drug–side effect gateway.” (2017).