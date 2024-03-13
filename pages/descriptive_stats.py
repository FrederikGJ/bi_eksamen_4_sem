import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    # Indlæs data
    data = pd.read_csv('data/csv/SDGSUICIDE.csv')

    # App titel
    st.title("Mental health and suicide rates in the world")

    # Rå data preview
    st.subheader("Raw data preview")
    st.write(data.head())

    # Renset data preview
    st.subheader("Cleaned data preview")
    st.write("This data only has suicide rate for both sexes included and have empty columns removed.")
    cleaned_data = data[data['SEX (CODE)'] == 'BTSX'].dropna(axis=1, how='all')
    st.write(cleaned_data.head())

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

    # Visning af deskriptiv statistik med LaTeX
    st.latex(rf'''
    \text{{Estimated Mean = }} \bar{{x}} = \frac{{1}}{{n}}\sum_{{i=1}}^{{n}}x_i = \frac{{1}}{{{n}}} \cdot \sum_{{i=1}}^{{n}}x_i = {mean_value.round(2)}
    ''')
    st.latex(rf'''
    \text{{Estimated Standard Deviation = }} s = \sqrt{{\frac{{1}}{{n-1}}\sum_{{i=1}}^{{n}}(x_i - \bar{{x}})^2}} = \sqrt{{\frac{{1}}{{{n}-1}} \cdot {sum_x_minus_mean_squared.round(2)}}} = {std_dev.round(2)}
    ''')
    st.write(cleaned_data['Numeric'].describe())

    st.divider()

    # Plotting distribution of suicide rates per region
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='REGION (DISPLAY)', y='Numeric', data=cleaned_data)
    plt.title('Distribution of Suicide Rates per 100,000 by Region')
    plt.xlabel('Region')
    plt.ylabel('Suicide Rate per 100,000')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(plt)

    # Fortsatte plots...
    # Bemærk: Gentag plottinglogikken for de efterfølgende plots som ønsket. Den grundlæggende struktur er givet ovenfor.

