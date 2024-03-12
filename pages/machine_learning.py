import streamlit as st
import pandas as pd
import os
import json
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
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

    st.write("WRITE SOME SHIT ABOUT THE SENTMENT ANALYSIS ")

    sentiment_analysis(combined_letters())

###  Data Preprocessing - now we need to clean and vectorize the data  - maybe sentiment analysis
    
#### add the definition of vector from the linear algebra for non mathematicians book 

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


def sentiment_analysis(merged_file_path):
    # Load English model with spacytextblob for sentiment analysis
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')

    with open(merged_file_path, 'r') as file:
        text = file.read()  # Read the entire file as a single string

    # Perform sentiment analysis
    doc = nlp(text)
    sentiment = doc._.blob.polarity  # Get the overall polarity score

    # Display the sentiment analysis result
    st.write("Sentiment Analysis Result:")
    st.write(f"Polarity (from -1 to 1, where -1 is negative and 1 is positive): {sentiment}")

def combined_letters():
    
    # Load and parse the data from the file
    with open('data/collection_sui_notes/merged_data.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Each record is separated by a newline and starts with '{', so we need to join them correctly
    data = []
    record = ''
    for line in lines:
        if line.startswith('{') and record:
            # Parse the current record and add it to the list
            data.append(json.loads(record))
            record = line  # Start a new record
        else:
            record += line  # Continue building the current record
    if record:
        data.append(json.loads(record))  # Add the last record

    # Filter English notes and translations
    notes_with_translations = []
    for item in data:
        if 'suicideNote' in item and ('en' in item.get('lang', '') or 'English' in item.get('biography', '')):
            note = item['suicideNote']
            translation = item.get('translation', 'No translation available')
            notes_with_translations.append(f"English Note: {note}\nTranslation: {translation}\n")

    # Save to a single file
    combined_file = 'data/collection_sui_notes/combined_notes.txt'
    with open(combined_file, 'w', encoding='utf-8') as file:
        for entry in notes_with_translations:
            file.write(entry + "\n")


    return combined_file