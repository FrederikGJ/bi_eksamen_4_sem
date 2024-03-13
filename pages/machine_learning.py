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
    st.write("The original json files are available in our GitHub repository.")
    display_merged_data(merged_file_path)
    st.write("We chose to get the suicide letters from the text file for our sentiment analysis.")
    display_merged_data(process_and_merge_data(merged_file_path))

    st.divider()

    st.subheader("Natural Language Processing")
    st.write("A definiton of NLP:")
    st.write("""NLP (Natural Language Processing) is a field within artificial intelligence 
             that focuses on enabling computers to understand, interpret, and generate human language.
              It combines techniques from computer science and linguistics to bridge the gap between human
              communication and computer processing.""")
    st.write("The NLP process we use when doing sentiment analysis:")
    st.markdown("""
    1. Text Vectorization: The first step in many NLP tasks is to convert text into a form that computers can understand and work with. This step is called vectorization. In your code, when you process the text with nlp(text), internally a form of vectorization occurs, where text (words, sentences) is transformed into numerical vectors. This allows the machine to analyze the language using mathematical and statistical methods.

    ***Definition of a vector from the book Linear Algebra for Non-Mathematicians by Sapir:***
    > ”The Physicist’s definition”: An object that has a magnitude and a direction (a geometric definition).
    >
    > ”The Computer scientists’ definition”: An array of numbers (an arithmetic definition).
    >
    > ”The Mathematician’s definition”: An element of a vector space (an abstract definition).
                
    *Sapir, P B. (2020) Basic Linear Algebra for Non-Mathematicians. [Lecture notes]. Page 27*
                
    2. Language Model Application: Once the text is vectorized, the program uses a language model (here en_core_web_sm) to understand the contextual meaning of each word and sentence. The language model contains information about grammar, word meanings, and how words are typically combined in the language.

    3. Adding Sentiment Analysis: By adding spacytextblob to the spaCy pipeline, sentiment analysis is integrated into the process. TextBlob calculates the sentiment for the entire document, resulting in a polarity value. This value indicates whether the overall sentiment in the text is positive, neutral, or negative.

    4. Sentiment Evaluation: The polarity value obtained from TextBlob indicates the text's sentiment on a scale from -1 to 1. This step involves analyzing how the words in the text contribute to an overall emotional tone.

    5. Presentation of Results: The program then displays the result of the sentiment analysis, including the polarity value, providing users with a numerical representation of the text's emotional tone.
    """)
    
    st.divider()

    st.subheader("Sentiment analysis")

    st.write("We do a sentiment analysis with a word cloud. The word cloud is a visual representation of the most common words in the text. The more frequent a word is, the larger it appears in the word cloud.")
    
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
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        for filename in os.listdir(data_folder):
            if filename.endswith('.json'):
                filepath = os.path.join(data_folder, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        json_data = json.load(f)
                        json_str = json.dumps(json_data, indent=4)
                        txt_file.write(json_str + "\n\n")
                except json.JSONDecodeError as e:
                    print(f"Error processing {filename}: {e}")

def display_merged_data(merged_file_path):
    with open(merged_file_path, 'r', encoding='utf-8') as file:
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

    with open(merged_file_path, 'r', encoding='utf-8') as file:
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