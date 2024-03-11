import streamlit as st
import pandas as pd

def show():
    st.title("Machine learning")

    ## i need to do some machine learning with my suicide data the json files in perticular 

    # Read the JSON file into a DataFrame
    data = pd.read_json('/data/collection_sui_notes.json')

    # Display the DataFrame
    st.write(data)