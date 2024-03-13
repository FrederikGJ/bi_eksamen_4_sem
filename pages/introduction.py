import streamlit as st
import pandas as pd


def show():
    st.title("Mental health and suicide")

    st.subheader("Group: OLA_Gruppe14")
    
    st.write("- Frederik Geisler Johannessen")
    st.write("- Signe Krusell Larsen")
    st.write("- Natasja Karoline Duckfeldt Vitoft Nordstedt")

    st.markdown("""
        ## Structure of the project

        Our project is structured in the following manner.

        1. Introduction and Cleaned Data Preview
        2. Descriptive statistics
        3. PCA
        4. Regression
        5. Machine learning  
                      
        
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
        

        ### Causal Inference with the current data
        Causal inference in statistics relies on the ability to establish a cause-and-effect relationship between variables. However, bad data quality can severely compromise this process. Here are some key reasons why:

        1. Inaccurate data: If the data contains errors or inaccuracies, any analysis conducted, including causal inference, will be based on faulty information. This can lead to incorrect conclusions about the relationships between variables.

        2. Missing data: Gaps in the data can result in biased or incomplete analyses. Missing data can affect the estimation of parameters and lead to misleading inferences about causal relationships.

        3. Confounding variables: For causal inference, it's crucial to account for all relevant variables that might affect the relationship between the independent and dependent variables. Poor data quality might mean that some confounding variables are not measured or are inaccurately recorded, which can skew the results.

        4. Poor representativeness: If the data is not representative of the population or phenomenon being studied, the findings from the data cannot be generalized. This means that any causal relationship identified in the study may not actually exist in the larger context.

        5. Temporal ambiguity: Causal inference often requires clear temporal ordering between cause and effect. Poor data quality can lead to uncertainties in the timing of events, making it difficult to establish which variable is the cause and which is the effect.

        In summary, bad data quality undermines the validity and reliability of statistical analyses, making it challenging, if not impossible, to conduct accurate causal inference. Therefore we can't make any causal inference on what causes mental health problems based on the current data.


    """)
    st.divider()


    # Indlæs data
    data = pd.read_csv('data/csv/SDGSUICIDE.csv')
    data1 = pd.read_csv('data/csv/suicide.csv')
    data2 = pd.read_csv('data/csv/facilities2016.csv', delimiter= ';', na_values=[''])
    data3 = pd.read_csv('data/csv/humanResources2016.csv', delimiter= ';', na_values=[''])

    # Rå data preview
    st.subheader("Raw data preview")
    st.write("""
    In this section, we present the original form of the data as it was collected. Our data cleaning process involves several steps:

    1. Removal of non-descriptive columns: We eliminate columns containing non-informative data, such as URLs or other irrelevant information.
    2. Handling missing values: We address NaN (Not a Number) values by either removing or replacing them with appropriate substitutes.
    3. Conversion to numeric: We convert relevant data values into numeric format, facilitating statistical analysis and visualization.

    By undertaking these cleaning procedures, we ensure the integrity and reliability of the data for subsequent analysis and interpretation.
    """)
    st.write(" **Tabel 1: Suicide data from 2019** ")
    st.write(data.head())
    st.write(" **Tabel 2: Suicide data from 1987 - 2016** ")
    st.write(data1.head())
    st.write(" **Tabel 3: Mental health facilities data from 2016** ")
    st.write(data2.head()) 
    st.write(" **Tabel 4: Human ressources data from 2016**")
    st.write(data3.head())
    st.divider()

    # Renset data preview
    st.subheader("Cleaned data preview")

    st.write(" **Tabel 1: Suicide data from 2019.** ")
    st.write("Gender has been standardized to include both sexes (BTSX). Non-informative columns have been eliminated, and rows containing null values have been excluded.")
    columns_to_remove = ['GHO (CODE)', 'GHO (DISPLAY)', 'GHO (URL)', 'PUBLISHSTATE (CODE)', 'PUBLISHSTATE (DISPLAY)', 'PUBLISHSTATE (URL)', 'YEAR (CODE)', 'YEAR (URL)', 'REGION (CODE)', 'REGION (URL)', 'WORLDBANKINCOMEGROUP (CODE)', 'WORLDBANKINCOMEGROUP (URL)', 'COUNTRY (CODE)', 'COUNTRY (URL)', 'AGEGROUP (CODE)', 'AGEGROUP (URL)','SEX (DISPLAY)' 'SEX (URL)', 'Low', 'High', 'StdErr', 'StdDev', 'Comments']
    remove_columns = data.drop(columns=columns_to_remove, errors='ignore')
    cleaned_data = remove_columns[remove_columns['SEX (CODE)'] == 'BTSX'].dropna(axis=1, how='all')
    st.write(cleaned_data.head())
    st.session_state.cleaned_data = cleaned_data
    

    st.write(" **Tabel 2: Suicide data from 1987 - 2016.** ")
    st.write("Columns lacking descriptive relevance have been eliminated. Rows containing null values have been excluded.")
    columns_to_remove1 = ['year', 'suicides_no','country-year', 'HDI for year']
    remove_columns1 = data1.drop(columns = columns_to_remove1, errors ='ignore')
    cleaned_data1 = remove_columns1.dropna(axis=1, how='all')
    st.write(cleaned_data1.head())
    st.session_state.cleaned_data1 = cleaned_data1 # save data


    st.write(" **Tabel 3: Mental health facilities data from 2016** ")
    st.write("Columns deemed non-descriptive have been discarded. Rows containing null values have been omitted, resulting in the exclusion of certain countries.")
    columns_to_remove2 = ['Year']
    remove_columns2 = data2.drop(columns = columns_to_remove2, errors ='ignore')
    cleaned_data2 = remove_columns2.dropna()
    st.write(cleaned_data2.head())
    st.session_state.cleaned_data2 = cleaned_data2 # save data


    st.write(" **Tabel 4: Human ressources data from 2016** ")
    st.write("Columns deemed non-descriptive have been discarded. Rows containing null values have been omitted, resulting in the exclusion of certain countries.")
    columns_to_remove3 = ['Year'] 
    remove_columns3 = data3.drop(columns = columns_to_remove3, errors ='ignore')
    cleaned_data3 = remove_columns3.dropna()
    st.write(cleaned_data3.head())
    st.session_state.cleaned_data3 = cleaned_data3 # save data

    
    st.divider()



    
