---
template: custom/contentpage.html
hero_text: Engineering
hero_image1: https://static.igem.wiki/teams/5016/wiki/engineering-1.jpg
hero_image2: https://static.igem.wiki/teams/5016/wiki/blur-2-left.webp
hero_image3: https://static.igem.wiki/teams/5016/wiki/blank.png
hero_image4: https://static.igem.wiki/teams/5016/wiki/blur-1-right.webp
---

# Software Engineering Success in SEPIA

## Overview

Polypharmacy presents a complex and non-linear, but highly prevalent risk profile.\
It is also a highly intersectional issue, involving doctors, pharmacists, biologists, caregivers, regulators and pharma companies.\
To identify how we as bioinformaticians could make a meaningful contribution to this multifaceted issue, we first extensively researched the existing literature and reached out to key subject-matter experts.

To our surprise, we discovered that previous bioinformatics approaches for predicting drug-drug interactions had solely focused on patients taking two drugs at once, whereas a typical patient in a care setting might on average take 5-10 drugs.

We have outlined some of the more significant engineering cycles we completed.

## Agile Development

In order to tackle this problem we adhered to a the engineering design cycle, which is commonly found in synthetic biology but also in software engineering.\
We enhanced the engineering cycle using principles from Agile to incrase productivity in a fast paced software focused development team.

Agile is a software development methodology and set of principles that emphasize flexibility, collaboration, and customer-centricity to deliver high-quality software efficiently.\
It is an iterative and incremental approach to software development that contrasts with traditional, linear methodologies.\
Agile methodologies promote adaptability, transparency, and constant improvement throughout the development process.

Agile encourages delivering working software at the end of each iteration.\
This ensures that the software is always in a potentially shippable state, which can be released to customers whenever necessary. As such, we were forced to repeadelty go through the engineering cycle.

We found the agile-inspired workflow to work well for the project.\
Due to our small team size, it was paramount that taks were distributed and completed efficiently.\
Our implementaion of the agile engineering cycle demanded two weekly meetings for the devleopmemt teams. Teammembers were incetivised to dicuss more specific issues in smaller meetings, where only those who were needed had to be present.\
We aimed to iterate through an engineering once every two weeks, meaning everbydoy had four opportunities to show thier progress and recieve feedback.\

On the one hand we were able to dive deeply into the code and work on implementing novel machine learning techniques, but on the other hand the regular check-ins with other team members and collaborators grounded us to keep a view on the real-world problem we were working on.

<figure markdown>
  ![Image title](https://static.igem.wiki/teams/5016/wiki/engineering-001.jpeg){ width="1800" }
  <figcaption>The adaptaion of the engineering cycle for machine larning development that we adhered to for the course of our project</figcaption>
</figure>

## Cycle I - Adapt Existing Work

We all stand on the shoulders of giants.\
A great way to gain some intital insights into a topic as adapting something which already exists.

### Design I

As such, we initialized our development process by gaining an overview of previous work in this field.\
We decided to base our engineering project on a previous drug-drug interaction prediction pipeline `Decagon` using multimodal drug-protein and protein-protein interaction networks [^1].

Both the dataset used for training and the codebase of Decagon proved to be outdated, due to being created in 2016.\
Instead of extending an six-year-old codebase and forever locking our project into `tensorflow 2.7`, we chose to create a new training dataset from drug interaction adverse events reported to the FDA, and reimplement Decagon as our first deliverable.

### Build I

### Test I

### Learn I

For this, we had to extend the graph used by Decagon to incorporate the possibility of multiple drugs interacting at once.
In a simple graph, these kinds of relationships – more technically referred to as hyperedges – cannot be natively represented.

## Cycle II - Initial Build

### Design II

!!! example "Mapping out data structures and model architecture"
    <figure markdown>
    ![Image title](https://static.igem.wiki/teams/5016/wiki/model-design.jpg){ width="1800" }
    <figcaption>An adaptaion of the engineering cycle adapted for machine larning development that we adhered to for the course of our project</figcaption>
    </figure>


### Build II

### Test II

### Learn II

After implementing this in our second sprint, we found that the graph constructed to train the model would incorporate all of the information required, but crash during the training process because it was using more memory than our computers had.

High memory
model funcitons for pariwise interactions but not for real polypharmacy
sparse tensors (expalain)

## Cycle III - Final Build

### Design III

### Build III

### Test III

### Learn III


some changes


[^1]: Zitnik, Marinka, et al. "Modeling Polypharmacy Side Effects with Graph Convolutional Networks." Bioinformatics, vol. 34, no. 13, 2018, pp. i457-i466,  [https://doi.org/10.1093/bioinformatics/bty294](https://doi.org/10.1093/bioinformatics/bty294).
