# Introduction

## Mental health and suicide - global and personal perspectives

### The problem

You often read news about the mental health crisis among young people all over the world.
Some goes as far as calling it a mental health pandemic. In our project we want to investigate this,
by looking at quantitative data from the WHO (World Health Organisation) and qualitative data from
a collection of suicide notes.
We use suicide rates as a proxy for the mental health state of peoples across the globe. And the suicide notes to investigate the subjective mental state of someone who is severely depressed. So we look at the problem of mental health problems from both a macro and micro persepektive. Both the global and the local perspective.

The question we seek to answer: what are the soci-economic and personal causes of mental health problems?

### Data sources

We have found our quantitiative data at the WHO website. The qualitative data, the collection of suicide letters, were found in a github repository.

Links for the data is found in our repository in the data directory in the file Links.md

### Data quality

The data we have is epidemological and economic data from countries all over the world.
We were able to download the data in a csv format, making it easily available for data manipulation with the Python programming language and its many libraries.

In the data we are using from WHO, there are serious errors. The data quality for different countries varies immensely. Most countries do not have data on the total population. It is only the Scandinavian countries that have valid data on the total population with and data on things like the CPR number, centralised statitics agency, centralized source taxation and so on. These measures ensure accurate data gathering of every single individual and company in the country. Unfortunately the opposite is the case on a global scale. Data on populations of great quality is scarcely available.

Antoher road block for students not affiliated with a hospital is the access to the data. The data is not available for download for the general public. This is among other things because of the european GDPR regulation. So even though there are data of great quality og health data in Denmark (and other Scandinavian countries), it is not available for the general public.

In the EU efforts are made through Eurostat, to enhance data quality acorss the European Union. But this takes a lot of work and economic reasources. Projects of this magnitude are not possible for all nations across the globe. Because of the econimic burden associated with it.

But if it would ever be possible an implementation of something like European Statistics Code of Practice on a global level would enable data scientists all over the world, to do productive reaseach for the benefit of mankind. 

**The European European Statistics Code of Practice has 16 principles, which are the following**

> **Professional Independence**: Ensuring the independence of statistical authorities from political and other external interference.
> **Mandate for Data Collection and Access to Data**: Clear legal mandate for statistical authorities to collect and access data for European statistical purposes.
> **Adequacy of Resources**: Sufficient resources to meet European statistics requirements.
> **Commitment to Quality**: Continuous improvement of process and output quality by statistical authorities.
> **Statistical Confidentiality and Data Protection**: Guaranteeing the privacy and confidentiality of data providers and the information they provide.
> **Impartiality and Objectivity**: Development, production, and dissemination of statistics in an objective and transparent manner.
> **Sound Methodology**: Use of appropriate methodologies underpinning quality statistics.
> **Appropriate Statistical Procedures**: Implementation of suitable statistical procedures throughout statistical processes.
> **Non-excessive Burden on Respondents**: Minimization of response burden for respondents.
> **Cost Effectiveness**: Effective use of resources in statistical processes.
> **Relevance**: Meeting the needs of users with European statistics.
> **Accuracy and Reliability**: Portrayal of reality in a reliable and accurate manner by European statistics.
> **Timeliness and Punctuality**: Timely and punctual release of European statistics.
> **Coherence and Comparability**: Ensuring statistics are internally consistent and comparable across regions and countries.
> **Accessibility and Clarity**: Clear and understandable presentation of European statistics, with accessible supporting metadata and guidance.
> **Coordination and Cooperation**: Coordination and active cooperation within the European Statistical System to ensure the development, production, and dissemination of European statistics.


_European Statistical System Committee, 2017. European Statistics Code of Practice for the National Statistical Authorities and Eurostat (EU statistical authority). Adopted 16 November 2017. [online] Available at: [[URL](https://ec.europa.eu/eurostat/web/products-catalogues/-/ks-02-18-142)] [12/03/2024]._

### An epistemological persepctive

    # - realiability in the project - an epistemological view

### Causal Inference based on the data

    # causal inference (confounders) - RCT needed for someitng approximating a cirtain causal inference

### Structure of the project

Our project is structured in the following manner.

1. Introduction and Cleaned Data Preview
2. Descriptive statistics
3. PCA
4. Regression
5. Machine learning
