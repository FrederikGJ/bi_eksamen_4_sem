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

    pca, data_scaled = apply_pca(features)

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
    
    # Make new dataframe that has the first 4 principal components
    st.write('First 4 principal components')
    pca_df = pd.DataFrame(pca.transform(data_scaled)[:, :4], columns=[f'PC{i}' for i in range(1, 5)])
    st.write(pca_df)

    st.divider()

def apply_pca(data, n_components=None):
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
    
    return pca, data_scaled