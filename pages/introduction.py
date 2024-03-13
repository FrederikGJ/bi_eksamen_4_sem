import streamlit as st
import pandas as pd


def show():
    st.title("Mental health and suicide rates in the world")

    st.subheader("Group:")

    st.write("Group: OLA_Gruppe14")
    
    st.write("Group Members:")
    st.write("- Frederik Geisler Johannessen")
    st.write("- Signe Krusell Larsen")
    st.write("- Natasja Karoline Duckfeldt Vitoft Nordstedt")


    st.subheader("Introduction to our project")
    st.write("**MANGLER AT SKRIVE EN INTRO**")


    # Indlæs data
    data = pd.read_csv('data/csv/SDGSUICIDE.csv')
    data1 = pd.read_csv('data/csv/suicide.csv')
    data2 = pd.read_csv('data/csv/facilities2016.csv', delimiter= ';', na_values=[''])
    data3 = pd.read_csv('data/csv/humanResources2016.csv', delimiter= ';', na_values=[''])

    # Rå data preview
    st.subheader("Raw data preview")
    st.write("Tabel 1: Suicide data from 2019")
    st.write(data.head())
    st.write("Tabel 2: Suicide data from 1987 - 2016")
    st.write(data1.head())
    st.write("Tabel 3: Mental health facilities data from 2016")
    st.write(data2.head()) 
    st.write("Tabel 4: Human ressources data from 2016")
    st.write(data3.head())

    # Renset data preview
    st.subheader("Cleaned data preview")

    st.write("Tabel 1: Suicide data from 2019. ")
    st.write("Sex have been set to both genders (BTSX). Non-descriptive columns have been removed. Rows  with null values have been removed.")
    columns_to_remove = ['GHO (CODE)', 'GHO (DISPLAY)', 'GHO (URL)', 'PUBLISHSTATE (CODE)', 'PUBLISHSTATE (DISPLAY)', 'PUBLISHSTATE (URL)', 'YEAR (CODE)', 'YEAR (URL)', 'REGION (CODE)', 'REGION (URL)', 'WORLDBANKINCOMEGROUP (CODE)', 'WORLDBANKINCOMEGROUP (URL)', 'COUNTRY (CODE)', 'COUNTRY (URL)', 'AGEGROUP (CODE)', 'AGEGROUP (URL)','SEX (DISPLAY)' 'SEX (URL)', 'Low', 'High', 'StdErr', 'StdDev', 'Comments']
    remove_columns = data.drop(columns=columns_to_remove, errors='ignore')
    cleaned_data = remove_columns[remove_columns['SEX (CODE)'] == 'BTSX'].dropna(axis=1, how='all')
    st.write(cleaned_data.head())
    st.session_state.cleaned_data = cleaned_data
    

    st.write("Tabel 2: Suicide data from 1987 - 2016.")
    st.write("Non-descriptive columns have been removed. Rows  with null values have been removed.")
    columns_to_remove1 = ['year', 'suicides_no','country-year', 'HDI for year']
    remove_columns1 = data1.drop(columns = columns_to_remove1, errors ='ignore')
    cleaned_data1 = remove_columns1.dropna(axis=1, how='all')
    st.write(cleaned_data1.head())
    st.session_state.cleaned_data1 = cleaned_data1 # save data


    st.write("Tabel 3: Mental health facilities data from 2016")
    st.write("Non-descriptive columns have been removed. Rows  with null values have been removed (this has removed some countries).")
    columns_to_remove2 = ['Year']
    remove_columns2 = data2.drop(columns = columns_to_remove2, errors ='ignore')
    cleaned_data2 = remove_columns2.dropna()
    st.write(cleaned_data2.head())
    st.session_state.cleaned_data2 = cleaned_data2 # save data


    st.write("Tabel 4: Human ressources data from 2016")
    st.write("Non-descriptive columns have been removed. Rows  with null values have been removed (this has removed some countries).")
    columns_to_remove3 = ['Year'] 
    remove_columns3 = data3.drop(columns = columns_to_remove3, errors ='ignore')
    cleaned_data3 = remove_columns3.dropna()
    st.write(cleaned_data3.head())
    st.session_state.cleaned_data3 = cleaned_data3 # save data

    
    st.divider()

    # Forklaring af datakvalitetsudfordringer
    st.markdown("### Confounders: ")
    st.write("In the data we are using from WHO, there are serious confounders. The data quality for different countries varies immensely. Most countries do not have data on the total population. It is only the Scandinavian countries that have valid data on the total population with things like the CPR number, centralised source taxation, and so on. These measures ensure accurate data tracking of every single individual and company in the country.")

    
