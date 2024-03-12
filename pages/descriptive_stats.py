import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


def show():
    # App titel
    st.title("Descriptive statistics")
    st.write("In this section we will calculate descriptive statistics for the cleaned data sets.")
    
    # Access the cleaned data from the session state
    cleaned_data = st.session_state.cleaned_data
    cleaned_data1 = st.session_state.cleaned_data1
    cleaned_data2 = st.session_state.cleaned_data2
    cleaned_data3 = st.session_state.cleaned_data3

    # Display the cleaned data
    st.write("Tabel 1: Suicide data from 2019")
    st.write(cleaned_data)
    st.write("Tabel 2: Suicide data from 1987 - 2016")
    st.write(cleaned_data1)
    st.write("Tabel 3: Mental health facilities data from 2016")
    st.write(cleaned_data2)
    st.write("Tabel 4: Human ressources data from 2016")
    st.write(cleaned_data3)


    st.divider()

    # Deskriptiv statistik
    st.subheader("Descriptive data on the suicide rates in the cleaned data set")
    
    st.write("The equation below display calculations of the estimated mean and standard deviation for Tabel 1. ")
    
    # Tabel 1
    desc_stats = cleaned_data['Numeric'].describe()    
    n = desc_stats['count']
    mean_value = desc_stats['mean']
    std_dev = desc_stats['std']
    sum_x_minus_mean_squared = ((cleaned_data['Numeric'] - mean_value)**2).sum()

    # Tabel2
    desc_stats = cleaned_data1['suicides/100k pop'].describe()    
    n = desc_stats['count']
    mean_value = desc_stats['mean']
    std_dev = desc_stats['std']
    sum_x_minus_mean_squared = ((cleaned_data1['suicides/100k pop'] - mean_value)**2).sum()
   
   # Tabel 3
    desc_stats = cleaned_data2['Mental health units in general hospitals (per 100 000 population)'].describe()    
    n = desc_stats['count']
    mean_value = desc_stats['mean']
    std_dev = desc_stats['std']
    sum_x_minus_mean_squared = ((cleaned_data2['Mental health units in general hospitals (per 100 000 population)'] - mean_value)**2).sum()
   
   # Tabel 4
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

    st.subheader("Tabel 1: Suicide data from 2019") 
    st.markdown("This plot illustrates the statistical summary of suicide rates in 2019, adjusted to reflect the number of reported suicides per 100,000 population. ")
    st.write(cleaned_data['Numeric'].describe())

    st.subheader("Tabel 2: Suicide data from 1987 - 2016")
    st.markdown("This plot illustrates the statistical summary of suicide rates in a 20 year time period, adjusted to reflect the number of reported suicides per 100,000 population.")
    st.write(cleaned_data1['suicides/100k pop'].describe())

    st.subheader("Tabel 3: Mental health facilities data from 2016")
    st.markdown("This plot illustrates the statistical summary of the number of mental health units in 2016, adjusted to reflect the number  of Mental health units in general hospitals per 100,000 population")
    st.write(cleaned_data2['Mental health units in general hospitals (per 100 000 population)'].describe())

    st.subheader("Tabel 4: Human ressources data from 2016")
    st.markdown("This plot illustrates the statistical summary of the number of human ressources in 2016, adjusted to reflect the number of psychiatrists working in mental health sector per 100 000 population")
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

    st.divider()


    #Tabel 2
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='generation', y='suicides/100k pop', data=cleaned_data1)
    plt.title('Distribution of Suicide Rates per 100,000 by Generation in 2016')
    plt.xlabel('generation')
    plt.ylabel('suicides/100k pop')
    plt.xticks(rotation=45, ha="right")
    st.pyplot(plt)

    st.divider()

   # For Tabel 3 - Histogram for Mental health facilities data
    plt.figure(figsize=(10, 6))
    plt.barh(cleaned_data2['Countries, territories and areas'], cleaned_data2['Mental health units in general hospitals (per 100 000 population)'], color='#0C7BE5')
    plt.title('Histogram of Mental health units in general hospitals per 100,000 in 2016')
    plt.xlabel('Mental health units in general hospitals (per 100 000 population)')
    plt.ylabel('Countries, territories and areas')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(plt)

    st.divider()

    # Tabel 4 - Histogram for Human resources data
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    sns.histplot(cleaned_data3['Psychiatrists working in mental health sector (per 100 000 population)'], ax=axes[0, 0])
    axes[0, 0].set_title('Psychiatrists (per 100k)')
    sns.histplot(cleaned_data3['Nurses working in mental health sector (per 100 000 population)'], ax=axes[0, 1])
    axes[0, 1].set_title('Nurses (per 100k)')
    sns.histplot(cleaned_data3['Social workers working in mental health sector (per 100 000 population)'], ax=axes[1, 0])
    axes[1, 0].set_title('Social Workers (per 100k)')
    sns.histplot(cleaned_data3['Psychologists working in mental health sector (per 100 000 population)'], ax=axes[1, 1])
    axes[1, 1].set_title('Psychologists (per 100k)')
    st.pyplot(fig)

    st.divider()
     

    # K-means clustering
    




    


    

