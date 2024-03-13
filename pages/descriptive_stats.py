import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

def identify_outliers(df, column_name, threshold=3.5):
  z_scores = stats.zscore(df[column_name])
  outlier_mask = np.abs(z_scores) > threshold
  return df[~outlier_mask]

def show():
    # App titel
    st.title("Descriptive statistics")
    st.write("Through statistical summaries and visualizations, we aim to gain insights into different metrics, such as suicide rates, mental health facilities, and human resources in the mental health sector. ")
    
    # Access the cleaned data from the session state
    cleaned_data = st.session_state.cleaned_data
    cleaned_data1 = st.session_state.cleaned_data1
    cleaned_data2 = st.session_state.cleaned_data2
    cleaned_data3 = st.session_state.cleaned_data3




    # Deskriptiv statistik    
    # Tabel 1
    desc_stats = cleaned_data['Numeric'].describe()    
    n = desc_stats['count']
    mean_value = desc_stats['mean']
    std_dev = desc_stats['std']
    sum_x_minus_mean_squared = ((cleaned_data['Numeric'] - mean_value)**2).sum()
  
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
    st.write("The equation below display calculations of the estimated mean and standard deviation for Tabel 1. ")
    st.latex(rf'''
    \text{{Estimated Mean = }} \bar{{x}} = \frac{{1}}{{n}}\sum_{{i=1}}^{{n}}x_i = \frac{{1}}{{{n}}} \cdot \sum_{{i=1}}^{{n}}x_i = {mean_value.round(2)}
    ''')
    st.latex(rf'''
    \text{{Estimated Standard Deviation = }} s = \sqrt{{\frac{{1}}{{n-1}}\sum_{{i=1}}^{{n}}(x_i - \bar{{x}})^2}} = \sqrt{{\frac{{1}}{{{n}-1}} \cdot {sum_x_minus_mean_squared.round(2)}}} = {std_dev.round(2)}
    '''
    )


    st.divider()
    st.write("The following tables and plots provide a visual representation of the statistical summary of the datasets. ")

    st.subheader(" **Tabel 1: Suicide data from 2019** ") 
    st.write("* The median is lower than the mean suicide rate. This indicates that the distribution of suicide rates might be skewed towards higher values (positively skewed).")
    st.write("* The standard deviation suggests a significant spread in suicide rates across different regions/countries.") 
    st.write("* The wide range between min/max and the high maximum value hint at potential outliers that could significantly impact the mean.")        
    st.write(cleaned_data['Numeric'].describe())


    st.subheader(" **Tabel 3: Mental health facilities data from 2016** ")
    st.write(cleaned_data2['Mental health units in general hospitals (per 100 000 population)'].describe())

    st.subheader(" **Tabel 4: Human ressources data from 2016** ")
    st.write("* The average number of psychiatrists per 100,000 population is 121.52.") 
    st.write("* The standard deviation is indicating a significant spread in the number of psychiatrists across different regions/countries.")
    st.write("* While not explicitly shown in the table, the presence of a minimum value (1.13) and a maximum value (839) suggests a potentially skewed distribution. However, with only summary statistics, it's difficult to determine the exact shape (left- or right-skewed).")
    st.write(cleaned_data3['Psychiatrists working in mental health sector (per 100 000 population)'].describe())
   
    st.divider()

    # Plotting distribution of suicide rates per region
    #Tabel 1
    st.write(""" **What is a Z-score ?**
             
    A Z-score indicates how many standard deviations a data point is from the mean. A positive Z-score suggests that the data point is above the mean, while a negative Z-score indicates it is below the mean.
    Z-scores are commonly used to identify outliers in a dataset. Data points with Z-scores significantly greater than or less than a threshold value (typically 2 or 3) are considered outliers and may warrant further investigation.
    In our application, we utilize Z-score based outlier identification to ensure the integrity of our statistical analyses and to identify potential anomalies within the mental health data we explore.
    """)
    outlier_removal = st.checkbox('Remove outliers based on Z-scores?')
    if outlier_removal:
        cleaned_data = identify_outliers(cleaned_data.copy(), 'Numeric')  
        cleaned_data1 = identify_outliers(cleaned_data1.copy(), 'suicides/100k pop')  

        st.write(" * Changes after removing outliers: Distribution is less skewed and more tightly clustered. Reduced range in suicide rates. Mean or median now better represents the typical suicide rate. Might be easier to see regional patterns in suicide rates.")
        st.write(" * Important considerations: Removed outliers might represent important cases. Outlier removal can affect statistical tests.") 

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
    st.write("Here we can se that the number of mental health units per 100,000 population varies greatly between countries. Some countries, such as Ireland and Estonia, have over 600 mental health units per 100,000 population, while others, such as Mexico and Ghana, have fewer than 100.")
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
    st.write("The graphs show that the number of mental health employees per 100,000 population is pretty low in most countries. However, there are a few countries with a much higher number of mental health employees.")
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

    




    


    

