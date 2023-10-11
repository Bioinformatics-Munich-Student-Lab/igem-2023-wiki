# Human Practices: Our Work and the World

We investigated the profound impact of our work.\
This included a rigorous examination of the implications and importance of community engagement, ethical considerations, societal impact, regulatory frameworks, stakeholder engagement, open source, and responsible scientific innovation in our quest for positive change.

## Living with Polypharmacy

“I had to throw myself in the car and drive home because of the pain. It is like a cramp in the stomach”, a real case of an 80-year-old woman, taking ten medications simultaneously, living with and suffering from the adverse effects of polypharmacy.\
In addition to “allergic symptoms, diarrhoea, loss of hair, [...], nausea, dizziness, or fatigue”, patients experienced social isolation, and their “symptoms were not taken seriously by healthcare professionals” [1].

​​As we witness our grandparents diligently sorting their pills, we are confronted with a profound question: how do these medications, each with its own distinct biochemical signature and mechanisms of action, interact within the human body?\
What impact do these medications have in conjunction with more complex biologics and therapeutics?

## The Solution is Software

Polypharmacy is intrinsically tied to the vast reservoir of data and information that characterizes patients and human biology.\
In this context, knowledge-driven computational methods are not only justifiable but are essential tools for addressing the challenges posed by making predictions about polypharmacy.

## Communication Issues in Software Development for Healthcare and Biomedicine

Especially when developing software, consulting the end-user is vital.\
According to Dr. Muhammad Mamdani “AI is actually going to be useful when it is driven by people with problems”. “It has to come from end users, from clinicians, who struggle with problems day-to-day”.\
With “this whole AI-thing, we see a lot of research, but the research is often quite meaningless.” “The vast majority of published papers would never ever deploy because it is clear that they didn’t speak to the clinician, or the methods used weren’t optimal.” “There has to be a mesh between the two” [2].\
Hence, it became imperative for us to determine the actual user base for our tool and assess its demand.\
Additionally, we needed to identify the specifications and requirements necessary to meet this demand, and instead of imagining a problem that our users would have, solve actually existing problems.

## Bottom-up Development

As part of our investigation into entrepreneurship and commercial viability, we have determined two main user groups.
On the one hand, our model would be deployed in a healthcare setting, such as hospitals and care facilities, where it would be used by medical practitioners and professionals.\
On the other hand, academics, pharmaceutical scientists, and biologists would leverage our model to make predictions about how the compound or therapy they are developing fits into the complex system of the human body and infer how a cocktail of medications would interact with the human biochemistry and other compounds, minimizing risks and maximizing therapeutic benefits.\
Yet, there are even more indirect stakeholders and interest groups that should not be overlooked.\
These include but are not limited to patients, local communities, non-government organizations, governments, and environmental activists.

## Consulting the Experts

We consulted experts since their insights and expertise are crucial for developing effective software solutions in healthcare and biomedicine.\
Experts provide valuable guidance on understanding the complexities of polypharmacy, ensuring that the software meets the needs of medical practitioners, researchers, and other stakeholders.\
Their input helps bridge the gap between theoretical research and practical applications, enhancing the tool’s usability and impact in addressing real-world healthcare challenges.

## Healthcare Stakeholders

One of the most important stakeholders we identified are healthcare professionals and researchers.\
To foster collaboration and gain valuable insights, we proactively reached out to experts in the field. Notably, we engaged with Prof. Dr. Julia Stingl, a prominent figure in the healthcare and research community, especially in clinical pharmacology.
The meeting on May 20, 2023, in Aachen, Germany, focused on clinical pharmacology and data analysis.\
We were able to take away some important insights and key takeaways from the meeting.

### Machine ↔︎ Human Interface: Ease of Use and Accessibility

Navigating applications through a command-line interface (CLI) is a common and often straightforward task for computer scientists and software engineers.\
Biologists and medical practitioners typically excel in domains that prioritize patient care, research, and the application of medical knowledge. Their primary focus is not on the intricacies of computer science or software development.\
Instead, they dedicate their time and energy to understanding human biology, diagnosing diseases, and providing healthcare services.

Recognizing this disconnect, we made efforts to bridge the gap between computer scientists and professionals in the medical and biological fields.\
Through our conversations, it became clear that we needed to develop user-friendly graphical interfaces to simplify the interaction with our software tools, making them more accessible to a broader audience.\
By providing intuitive, visually oriented interfaces, these tools aim to empower biologists and medical practitioners to make predictions about a combination of drugs they are prescribing or about a structure or biologic they are developing without the need for extensive programming or technical skills.

The user interface (UI) will undergo testing in a clinical setting in the upcoming weeks. This testing phase represents a significant milestone in the development and implementation of the UI, as it allows for real-world evaluation of its functionality and usability in a clinical environment.\
After this initial testing phase, we need to ensure that SEPiA UI meets regulatory standards and develop a protocol for healthcare professionals to utilize SEPiA UI effectively.

!!! example "UI Demo Prototype"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/ui-demo-1.jpeg){ width=1800" }
    <figcaption>This is the initial prototype for the UI that healthcare professionals would use to interact with our model</figcaption>
    </figure>

### Capturing Complete Data

We gained many insights obvious to someone who has interacted with patients for many years but are unimaginable for a software engineer or machine learning developer.\
For example, contraceptives and asthma inhalers are often not properly documented in medical records since patients often regard these as a part of their everyday lives and not essential pharmacologically active medications.\
To address this issue, we have implemented a reminder feature in the user interface (UI) for doctors and patients for important, often forgotten drugs.

### Impact on Children

Another critical group of potential users we were made aware of is children. Children represent a distinct demographic with their own considerations regarding medication interactions.\
They have unique pharmacokinetics and pharmacodynamics due to their ongoing growth and development.\
Consequently, they are commonly prescribed different dosages and different medications. We investigated our dataset and determined no children were present. As such, our model would display a significant bias against children.\
Consequently, we do not recommend using our model to make predictions for children.\
It is difficult to assess if a finetuned model for children would even be possible since public data availability for said demographic is extremely low.

## Stakeholders in Academia

Our journey in exploring synthetic biology and bioinformatics led us to consult experts like Dr. Markus List.

Dr. List’s expertise in biomedicine and his contributions to drug repurposing opened up new horizons to our team.\
He underscored the significance of an inclusive approach, advocating for the creation and dissemination of accessible and robust models that can catalyze advancements in biomedicine.

Additionally, he shared valuable insights into various biomedical applications, such as the innovative approach of drug repurposing.\
Polypharmacy side-effect-based repurposing is an intriguing application of our model that we will be pursuing after laying the groundwork via an open-source, freely available foundation model.

## Drug Repurposing

Drug repurposing, also known as drug repositioning or drug reprofiling, is a strategy in the field of pharmaceutical research where existing drugs that were originally developed for one medical condition are investigated and potentially repurposed for the treatment of another condition. This approach is gaining prominence as it offers several advantages over developing entirely new drugs, such as cost savings, faster development timelines, and a potentially reduced risk of adverse effects since the safety profiles of these drugs are often well-established.
 
We aim to adapt SEPiA and incorporate it into [RePo4EU](https://repo4.eu/), a platform for mechanism-based drug repurposing with 28 partners from 10 countries.\
We could provide valuable insights into possible novel uses of existing medications by predicting interactions and effects in combination therapies. This could lead to collaborations with pharmaceutical companies, other research institutions, and synthetic biologists looking to asses possible interactions or find new use cases for a therapy they are developing.

## Drug Development

Predicting and managing the potential side effects of polypharmacy plays a crucial role in drug development.\
We have researched some way in which the polypharmacy side effect predictions made by SEPiA can be used in the drug development process.

### Early Safety Assessment

During the early stages of drug development, researchers can use SEPiA to assess the potential interactions and side effects of a new drug when combined with existing medications.\
This proactive approach allows for the identification of safety concerns before extensive clinical trials, potentially saving time and resources.

### Drug Candidate Selection

Predictive models can help in the selection of drug candidates that are less likely to cause adverse interactions when used in combination with other common medications.\
This can influence decisions regarding which drug candidates to advance in the development pipeline.

### Clinical Trial Design

Understanding the potential side effects and interactions that can arise from polypharmacy is essential when designing clinical trials.\
This knowledge can help in the selection of appropriate patient populations, dosages, and monitoring protocols, ensuring the safety and integrity of the trials.

### Combination Therapies

Drug developers can leverage predictive models to identify promising combinations of drugs that may have synergistic effects, especially in cases where polypharmacy is prevalent.\
This can lead to the development of combination therapies that offer enhanced therapeutic benefits while minimizing side effects.\
This point ties back into the drug repurposing applications described by Dr. Markus List.

### Regulatory Approval

Regulatory agencies like the FDA and EMA require a comprehensive assessment of a drug’s safety profile before approving it for the market.\
SEPiA can aid in providing robust data on potential polypharmacy interactions, supporting the regulatory approval process.

## Biologics Risk Assessment

A large part of synthetic biology is the development of therapeutics.\
This ties back to our original questions: “How do we predict interactions between biologics, drugs, and the human body.” A model like ours will help synthetic biologists and pharmacologists make more accurate assessments of the risks a patient faces when undergoing a specific therapy.

In drug development, especially the creation of biological drugs like monoclonal antibodies, understanding potential interactions with other medications patients may be taking is critical.

In cancer treatment, immunotherapies are becoming increasingly prevalent. Combining different immunotherapies and chemotherapy can be complex.\
Predicting side effects associated with polypharmacy in cancer therapy is vital to reduce patient risks and optimize the chances of success.

We know that the mechanisms by which therapies and drugs function vary immensely. As such, it is important to publish the model parameters so teams working on a novel treatment may finetune the model according to their needs.\
This is why we have made our mode available on HuggingFace, a “large open-source community that builds tools to enable users to build, train, and deploy machine learning models based on open-source code and technologies” [^3].\
Our model would act as a Foundation model for others, like future iGEM Teams (see Contribution), to build on.

## Project Management and the Power-Interest Grid

In order to manage our stakeholders, we implemented the Power-Interest Grid.

The Power-Interest Grid, also known as the Power-Interest Matrix, is a project management tool used to categorize stakeholders based on their level of influence (power) and their level of interest in a project.\
It helps project managers and teams better understand how to engage with and manage various stakeholders effectively.\
The grid typically has four quadrants, each representing a different category of stakeholders.

!!! example "Power-Interst Grid: How it works"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/power-interst-grid-001.jpeg){ width=800" }
    <figcaption>Group stakeholders into four categories</figcaption>
    </figure>

### High Power, High Interest (Manage Closely):

Stakeholders in this category have both a significant level of influence (power) and a high level of interest in the project.\
They are crucial to the project’s success and need to be actively managed and engaged with to ensure their needs and expectations are met.\
Communication with these stakeholders should be frequent and detailed to keep them informed and satisfied.

### High Power, Low Interest (Keep Informed):

Stakeholders in this category have a high level of influence (power) but a relatively low level of interest in the project.\
While they may not be actively engaged or interested in project details, they can still impact the project’s outcome.\
Project managers should keep these stakeholders informed about major developments and decisions to ensure they remain supportive and do not become disengaged.

### Low Power, High Interest (Keep Satisfied):

Stakeholders in this category have a high level of interest in the project but limited influence (power).\
They may not have the ability to make significant decisions or changes, but their support and satisfaction are essential.\
Regular communication and efforts to address their concerns can help maintain a positive relationship.

### Low Power, Low Interest (Monitor):

Stakeholders in this category have both low influence (power) and low interest in the project.\
They are not likely to impact the project significantly, and little effort is needed to engage with them.\
Monitoring their involvement is sufficient, and resources can be allocated more efficiently to higher-priority stakeholders.

By using the Power-Interest Grid, project managers can tailor their communication and engagement strategies for each stakeholder group, ensuring that resources and efforts are focused where they are most needed.\
It helps in building and maintaining positive relationships with stakeholders, managing potential risks, and ultimately contributing to the successful execution of the project.

## Stakeholders in the Power-Interest Grid

In order to identify who we should focus our attention on, we ranked our potential stakeholders in the Power-Interest Grid.

!!! example "Power-Interst Grid: Stakeholders"
    <figure markdown>
        ![Image title](https://static.igem.wiki/teams/5016/wiki/power-interst-grid-002.jpeg){ width=800" }
    <figcaption>Our (potential) stakeholders in the Power-Interst Grid</figcaption>
    </figure>

## Entrepreneurship and Commercial Viability

Encapsulating research within the framework of a startup represents an innovative and highly effective approach to bringing cutting-edge solutions to the front line and making it widely accessible to a broader audience.\
This would enable the translation of our research into a scalable software solution and expedite its availability to hospitals, healthcare providers, synthetic biologists, and biochemists.\

As such, we spoke to the Silicon Valley-based Venture Capital investor Mani Honigstein from [HoneystoneVC](https://www.honeystonevc.com/) about potential startup implementations.

More information is available on the [entrepreneurship](/munichbioinformatics/entrepreneurship) page, where we explored how we would commercialize our project.


[^1]: Mannheimer, Stina, et al. "Experiences of Patients Receiving Home Care and Living with Polypharmacy: A Qualitative Interview Study." BJGP Open, vol. 6, no. 2, 2022, [https://doi.org/10.3399/BJGPO.2021.0181](https://doi.org/10.3399/BJGPO.2021.0181).
[^2]: YouTube, YouTube, 2 Oct. 2023, [https://www.youtube.com/watch?v=pqbFRi5kC0k](https://www.youtube.com/watch?v=pqbFRi5kC0k).
[^3]: Shah, Anish. “An Introduction to Huggingface Transformers for NLP.” W&B, 16 Nov. 2022, [wandb.ai/int_pb/huggingface/reports/An-Introduction-To-HuggingFace-Transformers-for-NLP--VmlldzoyOTgzMjI5#:~:text=HuggingFace%20is%20a%20large%20open,other%20practitioners%2C%20via%20its%20toolkit.](wandb.ai/int_pb/huggingface/reports/An-Introduction-To-HuggingFace-Transformers-for-NLP--VmlldzoyOTgzMjI5#:~:text=HuggingFace%20is%20a%20large%20open,other%20practitioners%2C%20via%20its%20toolkit.)

