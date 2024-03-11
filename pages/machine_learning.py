import streamlit as st
import pandas as pd
import os
import json

def show():
    st.title("Machine Learning")

    st.write("In this section we will use machine learning to analyze qualitative data. The data is a collection of suicide notes. This can give us a better understanding of the subjective mental state of people comitting suicide.")

    # Define the data folder and the path to the merged file
    data_folder = "data/collection_sui_notes"
    merged_file_path = os.path.join(data_folder, "merged_data.txt")

    # Merge JSON files to a text file and display the merged data
    merge_json_to_txt(data_folder)
    display_merged_data(merged_file_path)

###  Data Preprocessing - now we need to clean and vectorize the data  - maybe sentiment analysis

def merge_json_to_txt(data_folder):
    txt_file_path = os.path.join(data_folder, "merged_data.txt")
    with open(txt_file_path, 'w') as txt_file:
        for filename in os.listdir(data_folder):
            if filename.endswith('.json'):
                filepath = os.path.join(data_folder, filename)
                try:
                    with open(filepath, 'r') as f:
                        json_data = json.load(f)
                        json_str = json.dumps(json_data, indent=4)
                        txt_file.write(json_str + "\n\n")
                except json.JSONDecodeError as e:
                    print(f"Error processing {filename}: {e}")

def display_merged_data(merged_file_path):
    with open(merged_file_path, 'r') as file:
        merged_data = file.read()
        st.text_area("Merged Data - in raw txt format", merged_data, height=100)


