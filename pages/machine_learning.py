import streamlit as st
from wordcloud import WordCloud
import os
import json
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import json
import matplotlib.pyplot as plt

def show():
    st.title("Machine Learning")

    st.write("""
             First we have a definition of machine learning. Then we will apply machine learning. 
             More speifically we will apply a NLP model to analyze qualitative data and give a 
             quantitative score
             to the subjective mental state of people committing suicide.
             """)

    st.markdown("""
                ### Machine Learning: A Definition

                Machine learning (ML) is a subfield of artificial intelligence (AI) that focuses on enabling 
                computers to learn and make predictions or decisions without being explicitly programmed.
                 Instead of writing extensive code with rules for every possible scenario, 
                machine learning algorithms use data to identify patterns and build models that perform tasks autonomously.
                """)

    st.write("""
             In this section we will use machine learning to analyze qualitative data. 
             The data is a collection of suicide notes. This can give us a better understanding of the 
             subjective mental state of people comitting suicide.
             """)
    st.divider()

    st.subheader("Displaying the qalitative data in raw text foramt")
    # Define the data folder and the path to the merged file
    data_folder = "data/collection_sui_notes"
    merged_file_path = os.path.join(data_folder, "merged_data.txt")

    # Merge JSON files to a text file and display the merged data
    merge_json_to_txt(data_folder)
    ####################################################
    # her skriver jeg at man kan læse json filerne i vores github 
    # repo med de tegn der er på de oriinale sprog
    ############################################
    display_merged_data(merged_file_path)
    ####################################################
    # her beskriver jeg hvilken data jeg vælger
    ############################################
    display_merged_data(process_and_merge_data(merged_file_path))

    st.divider()

    st.subheader("Natural Language Processing")
    st.write("""NLP (Natural Language Processing) is a field within artificial intelligence 
             that focuses on enabling computers to understand, interpret, and generate human language.
              It combines techniques from computer science and linguistics to bridge the gap between human
              communication and computer processing.""")
    
    #############################################################################################################################################
    st.title("#### add the definition of vector from the linear algebra for non mathematicians book and explain the NLP process")
#############################################################################################################################################

    st.divider()

    st.subheader("Sentiment analysis")
    
    sentiment_analysis(process_and_merge_data(merged_file_path))

    st.write("""
            The polarity score is sligtly positive. This is not expected beacuse the
             notes we analyze are suicide letters.

             Given the relatively small sample size (16) of letters we won't be making any strong 
             conlusions. But it could be interesting to understand why the polarity score isn't negative.

             One palusible explanation is that suicide letters are very domain specific
             and the model is not trained specifically for that. Another plausible explanation is that
             the people writing the letters are feeling relief beacuase they have wanted to commit suicide 
             for a long time. But without the involvement of mental helath professionals it is hard to say. 

             Further investigation could be interesting. Maybe a model trained with Reinforcement Leaning (RF) 
             made in colalboration with mental health professionals would give a more realistc score.
            """)


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
        st.text_area("Merged Data - in raw txt format", merged_data, height=200)


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


def process_and_merge_data(input_file_path):
    # Load and parse the data from the file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = []
    record = ''
    for line in lines:
        if line.startswith('{') and record:
            data.append(json.loads(record))
            record = line
        else:
            record += line
    if record:
        data.append(json.loads(record))

    # Filter English notes and translations
    english_notes = []
    translations = []
    for item in data:
        if 'suicideNote' in item and ('en' in item.get('lang', '') or 'English' in item.get('biography', '')):
            english_notes.append(item['suicideNote'])
        if 'translation' in item:
            translations.append(item['translation'])

    # Save to new files and then merge
            
    english_notes_file = 'data/collection_sui_notes/english_notes.txt'
    translations_file = 'data/collection_sui_notes/translations.txt'
    merged_file_path = 'data/collection_sui_notes/merged_data_final.txt'

    with open(english_notes_file, 'w', encoding='utf-8') as file:
        for note in english_notes:
            file.write(note + "\n")

    with open(translations_file, 'w', encoding='utf-8') as file:
        for translation in translations:
            file.write(translation + "\n")

    # Merge the two files
    with open(english_notes_file, 'r', encoding='utf-8') as file1, \
         open(translations_file, 'r', encoding='utf-8') as file2, \
         open(merged_file_path, 'w', encoding='utf-8') as merged_file:
        merged_file.write(file1.read() + file2.read())

    return merged_file_path

def sentiment_analysis(merged_file_path):
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')

    with open(merged_file_path, 'r') as file:
        text = file.read()

    doc = nlp(text)
    sentiment = doc._.blob.polarity

    # Textual sentiment analysis result
    st.write("Sentiment Analysis Result:")
    st.write(f"Polarity (from -1 to 1, where -1 is negative and 1 is positive): {sentiment}")

    st.divider()

    # Word Cloud of text input
    generate_wordcloud(text)

    st.divider()

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)