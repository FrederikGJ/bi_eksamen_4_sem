import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    # Indlæs data
    data = pd.read_csv('data/csv/SDGSUICIDE.csv')
    data1 = pd.read_csv('data/csv/suicide.csv')
    data2 = pd.read_csv('data/csv/facilities2016.csv', delimiter= ';', na_values=[''])
    data3 = pd.read_csv('data/csv/humanResources2016.csv', delimiter= ';', na_values=[''])

    # App titel
    st.title("This page contains Descriptive statistics")

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

    st.write("Tabel 1: Suicide data from 2019")
    st.write("Sex have been set to both genders (BTSX). Useless columns have been removed. Rows  with null values have been removed.")
    columns_to_remove = ['GHO (CODE)', 'GHO (DISPLAY)', 'GHO (URL)', 'PUBLISHSTATE (CODE)', 'PUBLISHSTATE (DISPLAY)', 'PUBLISHSTATE (URL)', 'YEAR (CODE)', 'YEAR (URL)', 'REGION (CODE)', 'REGION (URL)', 'WORLDBANKINCOMEGROUP (CODE)', 'WORLDBANKINCOMEGROUP (URL)', 'COUNTRY (CODE)', 'COUNTRY (URL)', 'AGEGROUP (CODE)', 'AGEGROUP (URL)','SEX (DISPLAY)' 'SEX (URL)', 'Low', 'High', 'StdErr', 'StdDev', 'Comments']
    remove_columns = data.drop(columns=columns_to_remove, errors='ignore')
    cleaned_data = remove_columns[remove_columns['SEX (CODE)'] == 'BTSX'].dropna(axis=1, how='all')
    st.write(cleaned_data.head())

    st.write("Tabel 2: Suicide data from 1987 - 2016")
    st.write("Useless columns have been removed. Rows  with null values have been removed.")
    columns_to_remove1 = ['year', 'suicides_no','country-year', 'HDI for year']
    remove_columns1 = data1.drop(columns = columns_to_remove1, errors ='ignore')
    cleaned_data1 = remove_columns1.dropna(axis=1, how='all')
    st.write(cleaned_data1.head())

    st.write("Tabel 3: Mental health facilities data from 2016")
    st.write("Useless columns have been removed. Rows  with null values have been removed (this has removed some countries).")
    columns_to_remove2 = ['Year']
    remove_columns2 = data2.drop(columns = columns_to_remove2, errors ='ignore')
    cleaned_data2 = remove_columns2.dropna()
    st.write(cleaned_data2.head())

    st.write("Tabel 4: Human ressources data from 2016")
    st.write("Useless columns have been removed. Rows  with null values have been removed (this has removed some countries).")
    columns_to_remove3 = ['Year'] 
    remove_columns3 = data3.drop(columns = columns_to_remove3, errors ='ignore')
    cleaned_data3 = remove_columns3.dropna()
    st.write(cleaned_data3.head())

    st.divider()

    # Forklaring af datakvalitetsudfordringer
    st.write("Confounders: In the data we are using from WHO, there are serious confounders. The data quality for different countries varies immensely. Most countries do not have data on the total population. It is only the Scandinavian countries that have valid data on the total population with things like the CPR number, centralised source taxation, and so on. These measures ensure accurate data tracking of every single individual and company in the country.")

    st.divider()

    # Deskriptiv statistik
    st.subheader("Descriptive data on the suicide rates in the cleaned data set")

    desc_stats = cleaned_data['Numeric'].describe()    
    n = desc_stats['count']
    mean_value = desc_stats['mean']
    std_dev = desc_stats['std']
    sum_x_minus_mean_squared = ((cleaned_data['Numeric'] - mean_value)**2).sum()

    desc_stats = cleaned_data1['suicides/100k pop'].describe()    
    n = desc_stats['count']
    mean_value = desc_stats['mean']
    std_dev = desc_stats['std']
    sum_x_minus_mean_squared = ((cleaned_data1['suicides/100k pop'] - mean_value)**2).sum()
   
    desc_stats = cleaned_data2['Mental health units in general hospitals (per 100 000 population)'].describe()    
    n = desc_stats['count']
    mean_value = desc_stats['mean']
    std_dev = desc_stats['std']
    sum_x_minus_mean_squared = ((cleaned_data2['Mental health units in general hospitals (per 100 000 population)'] - mean_value)**2).sum()
   
    desc_stats = cleaned_data3['Psychiatrists working in mental health sector (per 100 000 population)'].describe()    
    n = desc_stats['count']
    mean_value = desc_stats['mean']
    std_dev = desc_stats['std']
    sum_x_minus_mean_squared = ((cleaned_data3['Psychiatrists working in mental health sector (per 100 000 population)'] - mean_value)**2).sum()
   

    # Visning af deskriptiv statistik med LaTeX
    st.latex(rf'''
    \text{{Estimated Mean = }} \bar{{x}} = \frac{{1}}{{n}}\sum_{{i=1}}^{{n}}x_i = \frac{{1}}{{{n}}} \cdot \sum_{{i=1}}^{{n}}x_i = {mean_value.round(2)}
    ''')
    st.latex(rf'''
    \text{{Estimated Standard Deviation = }} s = \sqrt{{\frac{{1}}{{n-1}}\sum_{{i=1}}^{{n}}(x_i - \bar{{x}})^2}} = \sqrt{{\frac{{1}}{{{n}-1}} \cdot {sum_x_minus_mean_squared.round(2)}}} = {std_dev.round(2)}
    ''')
    st.write("Tabel 1: Suicide data from 2019")
    st.write(cleaned_data['Numeric'].describe())

    st.write("Tabel 2: Suicide data from 1987 - 2016")
    st.write(cleaned_data1['suicides/100k pop'].describe())

    st.write("Tabel 3: Mental health facilities data from 2016")
    st.write(cleaned_data2['Mental health units in general hospitals (per 100 000 population)'].describe())

    st.write("Tabel 4: Human ressources data from 2016")
    st.write(cleaned_data3['Psychiatrists working in mental health sector (per 100 000 population)'].describe())
   
    st.divider()

    # Plotting distribution of suicide rates per region
    #Tabel 1
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='REGION (DISPLAY)', y='Numeric', data=cleaned_data)
    plt.title('Distribution of Suicide Rates per 100,000 by Region in 2019')
    plt.xlabel('Region')
    plt.ylabel('Suicide Rate per 100,000')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(plt)

    #Tabel 2
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='generation', y='suicides/100k pop', data=cleaned_data1)
    plt.title('Distribution of Suicide Rates per 100,000 by Generation in 2016')
    plt.xlabel('generation')
    plt.ylabel('suicides/100k pop')
    plt.xticks(rotation=45, ha="right")
    st.pyplot(plt)

    #Tabel 3
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Countries, territories and areas', y='Mental hospitals (per 100 000 population)', data=cleaned_data2)
    plt.title('Distribution of Mental hospitals per 100,000 by Region in 2016')
    plt.xlabel('Countries, territories and areas')
    plt.ylabel('Mental hospitals (per 100 000 population)')
    plt.xticks(rotation=45, ha="right")
    st.pyplot(plt)

    #Tabel 4
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Countries, territories and areas', y='Psychiatrists working in mental health sector (per 100 000 population)', data=cleaned_data3)
    plt.title('Distribution of Human resources per 100,000 by Region in 2016')
    plt.xlabel('Countries, territories and areas')
    plt.ylabel('Psychiatrists working in mental health sector (per 100 000 population)')
    plt.xticks(rotation=45, ha="right")
    st.pyplot(plt)

    

