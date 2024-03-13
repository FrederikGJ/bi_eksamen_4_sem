import streamlit as st
from pages import descriptive_stats, introduction, pca, regression, machine_learning, cleaning_data  # Importer siderne



# Funktioner for hver side
pages = {
    "Introduction": introduction.show,
    "Cleaned data": cleaning_data.show,
    "Descriptive statistics": descriptive_stats.show,
    "PCA": pca.show,
    "Regression": regression.show,
    "Machine learning": machine_learning.show,
}

# Hovedapp
def main():
    st.sidebar.title("Contents")
    page = st.sidebar.radio("Go to", list(pages.keys()))

    # Vis den valgte side
    pages[page]()  




if __name__ == "__main__":
    main()
