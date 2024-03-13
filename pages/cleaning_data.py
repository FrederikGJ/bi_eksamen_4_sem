import streamlit as st
import pandas as pd

def show():

     # Indlæs alle datasæt 
    facilities = pd.read_csv('data/csv/facilities2016.csv', sep=';')
    humanRessources = pd.read_csv('data\csv\humanResources2016.csv', sep=';')
    suicide2019 = pd.read_csv('data/csv/suicide.csv')
    suicide2016 = pd.read_csv('data/csv/SDGSUICIDE.csv')
    suicideData2016 = pd.read_csv('data\csv\SucicideData2016.csv')

    st.title("Data cleaning")

    ###################################################################################################################################

    # FACILITIES 

    st.markdown("<h4 style='color:blue;'> Facilities 2016 </h4>", unsafe_allow_html=True)

    st.write("Before being cleaned:")
    st.write(facilities.head())
    st.write("Shape:")
    st.write(facilities.shape)
    st.write("Columns:")
    st.write(facilities.columns)

    st.write("Check for empty columns:")
    st.write(facilities.isnull().sum())
    
    # Display rows with missing values
    st.write("Display rows with missing values")
    rows_with_missing_values_facilities = facilities[facilities.isnull().any(axis=1)]
    st.write(rows_with_missing_values_facilities)

    # Dropping some columns
    columns_to_drop = ['Mental health day treatment facilities (per 100 000 population)', 'Community residential facilities (per 100 000 population)']
    facilities = facilities.drop(columns=columns_to_drop)
    st.write(facilities.head())

    st.write("After dropping columns:")
    st.write(facilities.head())

    # Calculate the median for each column with missing values
    median_values = facilities[['Mental hospitals (per 100 000 population)',
                            'Mental health units in general hospitals (per 100 000 population)',
                            'Mental health outpatient facilities (per 100 000 population)']].median()

    # Replace missing values with the median
    facilities.fillna(median_values, inplace=True)

    st.write("After replacing missing values with median:")
    st.write(facilities.head())

    ###################################################################################################################################

    # HUMAN RESOURCES
    
    st.markdown("<h4 style='color:blue;'> Human Resources 2016 </h4>", unsafe_allow_html=True)

    st.write("Before being cleaned:")
    st.write(humanRessources.head())
    st.write("Shape:")
    st.write(humanRessources.shape)
    st.write("Columns:")
    st.write(humanRessources.columns)
    
    st.write("Check for empty columns:")
    st.write(humanRessources.isnull().sum())

    # Display rows with missing values
    st.write("Display rows with missing values")
    rows_with_missing_values_humanRessources = humanRessources[humanRessources.isnull().any(axis=1)]
    st.write(rows_with_missing_values_humanRessources)

    # Dropping some columns
    columns_to_drop = ['Social workers working in mental health sector (per 100 000 population)']
    humanRessources = humanRessources.drop(columns=columns_to_drop)
    st.write(humanRessources.head())

    st.write("After dropping columns:")
    st.write(humanRessources.head())

    # Calculate the median for each column with missing values
    median_values = humanRessources[['Psychiatrists working in mental health sector (per 100 000 population)',
                            'Nurses working in mental health sector (per 100 000 population)',
                            'Psychologists working in mental health sector (per 100 000 population)']].median()

    # Replace missing values with the median
    humanRessources.fillna(median_values, inplace=True)

    st.write("After replacing missing values with median:")
    st.write(humanRessources.head())

    ###################################################################################################################################

    # SUICIDE 1987 - 2019

    st.markdown("<h4 style='color:blue;'> Suicide 2019 </h4>", unsafe_allow_html=True)

    st.write("Before being cleaned:")
    st.write(suicide2019.head())
    st.write("Shape:")
    st.write(suicide2019.shape)
    st.write("Columns:")
    st.write(suicide2019.columns)

    st.write("Check for empty columns")
    st.write(suicide2019.isnull().sum())

    age_groups = suicide2019['age'].unique()
    sex_groups = suicide2019['sex'].unique()
    generation_groups = suicide2019['generation'].unique()

    # Print or display the unique age groups
    st.write("Age groups:")
    st.write(age_groups)

    # Print or display the unique gender groups
    st.write("Gender groups:")
    st.write(sex_groups)

    st.write ("Generations:")
    st.write(generation_groups)

     # Dropping some columns
    columns_to_drop = ['HDI for year', 'country-year']
    suicide2019 = suicide2019.drop(columns=columns_to_drop)
    suicide2019.to_csv('data/csv/suicidesBeforeMapping.csv', index=False)

    # Dropping some columns
    columns_to_drop = ['HDI for year', 'generation', 'country-year']
    suicide2019 = suicide2019.drop(columns=columns_to_drop)
    st.write(suicide2019.head())

    # Mapping
    gender_mapping = {'female': 0, 'male': 1}
    suicide2019['sex'] = suicide2019['sex'].map(gender_mapping)

    st.write("After mapping:")
    st.write(suicide2019.head())

    age_mapping = {'5-14 years': 0, '15-24 years': 1, '25-34 years': 2, '35-54 years': 3, '55-74 years': 4, '75+ years': 5}
    suicide2019['age'] = suicide2019['age'].map(age_mapping)

    st.write("After mapping:")
    st.write(suicide2019.head())

    suicide2019.to_csv('data/csv/suicide2019_cleaned.csv', index=False)

    suicide2016 = suicide2019[suicide2019['year'] == 2016]

    st.write("Suicide data for the year 2016:")
    st.write(suicide2016.head())

    # New CSV files with cleaned data
    suicide2016.to_csv('data/csv/suicide2016_cleaned.csv', index=False)
    facilities.to_csv('data/csv/facilities2016_cleaned', index=False)
    humanRessources.to_csv('data/csv/humanRessources2016_cleaned', index=False)


    st.markdown("<h4 style='color:blue;'> All datasets cleaned </h4>", unsafe_allow_html=True)

    st.write("Sucicide 2016:")
    st.write(suicide2016.head())
    st.write("Facilities 2016:")
    st.write(facilities.head())
    st.write("Human ressources 2016:")
    st.write(humanRessources.head())


    # Merge facilities and humanRessources on the "Countries, territories and areas" and "Year" columns
    merged_data = pd.merge(facilities, humanRessources, on=["Countries, territories and areas", "Year"], how="inner")

    # Merge the result with suicide2016 on the "country" and "year" columns
    final_data = pd.merge(merged_data, suicide2016, left_on=["Countries, territories and areas", "Year"], right_on=["country", "year"], how="inner")

    # Drop the redundant "country" and "year" columns
    final_data.drop(["country", "year"], axis=1, inplace=True)

    st.write("Datasets combined:")
    st.write(final_data.head(20))

    final_data.to_csv('data/csv/suicide2016withfacilities.csv', index=False)

    ####################################################################################################################################################################################################################
