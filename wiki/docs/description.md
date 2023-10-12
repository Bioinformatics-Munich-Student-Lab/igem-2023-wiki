---
template: custom/contentpage.html
hero_text: Description
hero_image1: https://static.igem.wiki/teams/5016/wiki/kevin-chin-pymrarrunx0-unsplash-db-1.jpg
hero_image2: https://static.igem.wiki/teams/5016/wiki/blur-2-left.webp
hero_image3: https://static.igem.wiki/teams/5016/wiki/blank.png
hero_image4: https://static.igem.wiki/teams/5016/wiki/blur-1-right.webp
---

# Project Description

## Abstract

A patient is described as undergoing polypharmacy if they simultaneously take more than five medications. While often necessary for treating multimorbid or vulnerable patients, polypharmacy is associated with various risks such as adverse drug interactions, increased incidence and severity of side effects, poor compliance, and decline in the patient's quality of life[^1].

Polypharmacy presents a distinct and frequently non-linear side effect profile that is, in many cases, still poorly understood, which affects 15% of the general population in the U.S. and about 10-20% in different European countries, with the incidence of polypharmacy rising sharply with age and poor health; in care settings, polypharmacy incidences above 50% are not uncommon[^2]^,^[^3]. Additionally, with the increasing life expectancy worldwide [^7], understanding polypharmacy will only become more critical in the coming years. 

Because the number of possible combinations of different drugs increases exponentially with the number of drugs a patient takes, systematic laboratory testing is impractical. Computational approaches have only focused on pairwise drug-drug interactions [^10]^,^[^11]. Therefore, a computational approach is needed to extend current methodologies to arbitrary numbers of drugs.

Our project aims to use advanced graph-based deep learning algorithms applied to polypharmacy hypergraphs and chemical language models [^13] for predicting the effects of many drugs interacting. Using this approach, we reach AUROC 0.895 using a pairwise drug-drug interaction dataset from Dacagon[^10] and 0.982 for multi-drug polypharmacy interactions.


!!! example "Trends in Polypharmacy"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/plot1-dark.png){ width=600" }
    <figcaption>Trends in polypharmacy among adults in the Netherlands 1999–2014, stratified by age.[^6]</figcaption>
    </figure>


## Motivation

Our team was deeply motivated to choose this project because of the personal experiences many of us have had with elderly family members, particularly our grandparents. Witnessing our grandparents taking a plethora of medications at once, with sometimes more than five just for breakfast, sparked a sense of concern and curiosity among us. It made us question the safety and efficacy of such an approach and led us to investigate polypharmacy. So, we aid in identifying potential drug combinational interactions systematically, which would be beneficial in the early drug discovery/design process in the synthetic biology field, improving the efficacy-safety balance of the drug and facilitating the optimal candidate for the design of the drug's chemical structure with minimal adverse effects.

Socially, polypharmacy affects the quality of life of a large section of the population. Over 80% of nursing home residents[^4] and over 70% of hospitalized patients[^5] are affected by polypharmacy. This indicates that a significant proportion of the community is at risk of adverse drug reactions, impacting not just their health but also the well-being of their families. Seeing the gravity of the situation and the role polypharmacy plays in the lives of our loved ones, we concluded that we ought to focus our efforts on alleviating the problem.

## Approach
We predict true polypharmacy interactions by first building a hypergraph where drugs share a hyperedge, which results in a specific effect when taken together. Additionally, drugs can share direct edges when the chemical language model embeddings indicate similar structures. This hypergraph is transformed into a standard graph by introducing hypernodes. The model is then trained to aggregate information from the graph structure around the drugs in question and combine these with information about the potential effect. Finally, these embeddings are combined by multiplying the embeddings and passed through a one-layer neural network. The resulting score indicates the likelihood that the given combination of drugs can cause the given side effect.


## Applications
Our vision is to use our model to provide doctors with the tools to not harm by prescribing safe and healthy combinations of drugs, improving patient quality of life. We have established a close partnership with the Department of Clinical Pharmacology at the University Hospital Aachen in Germany to make this vision a reality. This collaboration allows us to gather input from key medical stakeholders to deliver a practical, easy-to-use software that can empower the medical community from the get-go. Through the network of RWTH Aachen, we could also deploy our model in other German university hospitals and, ultimately, internationally.




[^1]: Van Wilder L, Devleesschauwer B, Clays E, Pype P, Vandepitte S, De Smedt D. Polypharmacy and Health-Related Quality of Life/Psychological Distress Among Patients With Chronic Disease. Prev Chronic Dis 2022;19:220062. [http://dx.doi.org/10.5888/pcd19.220062](http://dx.doi.org/10.5888/pcd19.220062).
[^2]: Lee, Georgie, et al. "The Patterns and Implications of Potentially Suboptimal Medicine Regimens among Older Adults: a Narrative Review." Therapeutic Advances in Drug Safety, 2022, [https://doi.org/10.1177/20420986221100117](https://doi.org/10.1177/20420986221100117).
[^3]: Kantor ED, Rehm CD, Haas JS, Chan AT, Giovannucci EL. Trends in Prescription Drug Use Among Adults in the United States From 1999-2012. [https://doi.org/10.1001/jama.2015.13766](https://doi.org/10.1001/jama.2015.13766).
[^4]: Calcaterra, Laura, et al. "Predictors of Drug Prescription in Nursing Home Residents: Results from the INCUR Study." Internal and Emergency Medicine, vol. 17, no. 1, 2022, pp. 165-171,  [https://doi.org/10.1007/s11739-021-02841-6](https://doi.org/10.1007/s11739-021-02841-6).
[^5]: Trumic, Edisa, et al. "Prevalence of Polypharmacy and Drug Interaction Among Hospitalized Patients: Opportunities and Responsabilities in Pharmaceutical Care." Materia Socio-Medica, vol. 24, no. 2, 2012, pp. 68-72,  [https://doi.org/10.5455/msm.2012.24.68-72](https://doi.org/10.5455/msm.2012.24.68-72).
[^6]: Oktora, Monika, et al. "Trends in Polypharmacy and Dispensed Drugs among Adults in the Netherlands as Compared to the United States." PLOS ONE, vol. 14, no. 3, 2019, p. e0214240,  [https://doi.org/10.1371/journal.pone.0214240](https://doi.org/10.1371/journal.pone.0214240).

[^7]: WHO https://www.who.int/data/gho/data/themes/mortality-and-global-health-estimates/ghe-life-expectancy-and-healthy-life-expectancy

[^8]:Midão, L., Giardini, A., Menditto, E., Kardas, P., & Costa, E. (2018). Polypharmacy prevalence among older adults based on the survey of health, ageing and retirement in Europe. Archives of Gerontology and Geriatrics, 78, 213-220. https://doi.org/10.1016/j.archger.2018.06.018

[^9]:Zhang N, Sundquist J, Sundquist K, Ji J. An Increasing Trend in the Prevalence of Polypharmacy in Sweden: A Nationwide Register-Based Study. Front Pharmacol. 2020 Mar 18;11:326. doi: 10.3389/fphar.2020.00326. PMID: 32265705; PMCID: PMC7103636. 

[^10]: Decagon. Marinka Zitnik, Monica Agrawal, Jure Leskovec, Modeling polypharmacy side effects with graph convolutional networks, Bioinformatics, Volume 34, Issue 13, July 2018, Pages i457–i466, https://doi.org/10.1093/bioinformatics/bty294

[^11]: Simvec. Lukashina, N., Kartysheva, E., Spjuth, O. et al. SimVec: predicting polypharmacy side effects for new drugs. J Cheminform 14, 49 (2022). https://doi.org/10.1186/s13321-022-00632-5

[^12]: nSides. Vanguri, Rami; Romano, Joseph; Lorberbaum, Tal; Youn, Choonhan; Nwankwo, Victor; Tatonetti, Nicholas (2017). nSides: An interactive drug--side effect gateway. figshare. Dataset. https://doi.org/10.6084/m9.figshare.5483698.v2

[^13]: Molformer. Large-Scale Chemical Language Representations Capture Molecular Structure and Properties
Jerret Ross, Brian Belgodere, Vijil Chenthamarakshan, et al. https://arxiv.org/abs/2106.09553 