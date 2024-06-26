import streamlit as st
from pages import descriptive_stats, introduction, pca, regression, machine_learning# Importer siderne



# Funktioner for hver side
pages = {
    "Introduction": introduction.show,
    "Descriptive statistics": descriptive_stats.show,
    "Regression": regression.show,
    "PCA": pca.show,
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
