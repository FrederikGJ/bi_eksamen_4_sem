import streamlit as st
from pages import descriptive_stats, introduction, cleaning_data, pca, regression, machine_learning  # Importer siderne

# lolo frederiks branch

# Funktioner for hver side
pages = {
    "Introduction": introduction.show,
    "Cleaning data": cleaning_data.show,
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
