import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

def show():
    st.title("Principal Component Analysis with Singular Value Decomposition")

    st.write("Principal Component Analysis (PCA) is a method used to reduce the dimensionality of data. It is a method that is often used in machine learning to reduce the number of features in a dataset.")
    st.write("First we will load the dataset and clean it up a bit. Then we will perform PCA on the dataset and visualize the results.")
    st.divider()

    # Load data from CSV
    data = pd.read_csv("data/csv/suicide.csv")

    st.write("Data raw")
    st.write(data.head())

    # Filter the data to keep only the entries from the year 2014
    data_2014 = data[data['year'] == 2014]

    # Convert 'male' to 1 and 'female' to 0
    st.write("We choose the data from 2014 and convert gender data to numeric values (female 0 and male 1)")
    data_2014['sex'] = data_2014['sex'].map({'male': 1, 'female': 0})

    # Remove columns with all NaN values 
    data_2014 = data_2014.dropna(axis=1, how='all')

    # Alternate remaining NaN data to the value 0
    data_2014 = data_2014.fillna(0)

    st.write(data_2014.head())

    features = data_2014.drop(columns=['country'])

    numeric_features = data_2014.select_dtypes(include=[np.number]) # Make sure this is defined
    pca, data_scaled, loadings = apply_pca(features, numeric_features) 


    st.divider()

    st.subheader('PCA')
    
    # Correct the plot to dynamically match the number of PCA components
    n_components = pca.n_components_
    fig, ax = plt.subplots()
    ax.bar(range(1, n_components + 1), pca.explained_variance_ratio_)
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')
    ax.set_title('PCA - Explained Variance Ratio - scree plot')
    st.pyplot(fig)
    st.write("The plot shows the eigenvalues of the each principal component. The eigenvalues are the variance of the original data projected onto the principal components. ")
    
    # Make new dataframe that has the first 4 principal components
    st.write('First 4 principal components - projection of each data point onto the principal components.')
    pca_df = pd.DataFrame(pca.transform(data_scaled)[:, :4], columns=[f'PC{i}' for i in range(1, 5)])
    st.write(pca_df)

    st.subheader('Loading scores')
    loadings_df = pd.DataFrame(loadings,  
        columns=numeric_features.columns, 
        index=[f'PC{i}' for i in range(1, n_components + 1)])
    st.write(loadings_df)

    st.write("Loading scores are the weights of the original features in the principal components. They are used to interpret the principal components. The loading scores are the coefficients of the linear combination of the original features that make up the principal components. They are also called the eigenvectors of the covariance matrix of the original features. The loading scores are the weights of the original features in the principal components. They are used to interpret the principal components. The loading scores are the coefficients of the linear combination of the original features that make up the principal components.")
    st.divider()

    st.subheader("Interpretation of Loading Scores of the First Two Principal Components")

    st.write("**PC1**")
    st.write("""
    * **Positive loadings:**
        * suicides/100k pop: Higher loadings here suggest PC1 is likely influenced by variations in suicide rates per capita.
        * population: A positive loading here means that countries with higher populations tend to also have higher suicide rates per capita (as reflected in the suicides/100k pop feature). 
    * **Negative loading:** 
        * HDI for year: A negative loading here suggests that countries with higher Human Development Index (HDI) tend to have lower suicide rates per capita (reflected in the suicides/100k pop feature). 
    """)

    st.write("**PC2**")
    st.write("""
    * **Positive loadings:**
        * gdp_per_capita ($): Countries with higher GDP per capita tend to have higher scores on PC2.
    * **Negative loadings:**
        * suicides_no: Negative loading indicates that higher numbers of suicides are associated with lower scores on PC2.
    """) 
    st.write("The above interpretation tells us that highler living standards and GDP pr capita leads to fewer suicide. This could indicate that mental health is effected by the economic opportunities of the individuals living there. But also that more developed nations with better healthcaresystems might prevent suicides. These are not strong conlusions. But might be interesting points for further investigation with higher quality data.")
    st.divider

 

def apply_pca(data,numeric_features, n_components=None):
    # Ensure data is numeric
    numeric_features = data.select_dtypes(include=[np.number])
    
    # Adjust n_components based on the numeric features only
    if n_components is None or n_components > min(numeric_features.shape):
        n_components = min(numeric_features.shape[0], numeric_features.shape[1]) - 1 
    
    # Standardize the numeric data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(numeric_features)
    
    # Apply PCA
    pca = PCA(n_components=n_components)
    pca.fit(data_scaled) 

    # Get loading scores
    loadings = pca.components_

    return pca, data_scaled, loadings 