import streamlit as st
import pandas as pd

def show():

     # Indlæs data 
    suicide2019 = pd.read_csv('data/csv/suicide.csv')

    # SUICIDE 1987 - 2019

    st.subheader("Sucicide")

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

    st.write("After being cleaned:")
    st.write(suicide2019.head())

####################################################################################################################################################################################################################
