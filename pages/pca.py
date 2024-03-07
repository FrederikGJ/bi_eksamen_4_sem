import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

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

    st.write(data_2014.head())

 

