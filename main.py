import pickle
import streamlit as st
import numpy as np
import pandas as pd

books=pickle.load(open("20books.pkl","rb"))

rad=st.sidebar.radio("Navigation",["Home","About"])

if rad=="Home":
    st.title("BookScraper")
    st.header("Let's find similar books for you")
    def get_name(text,v):
        N=books[books['Title']==text]['Recommended_Books'].values[0]
        for i in range (v):
            title_container = st.beta_container()
            col1, col2 = st.beta_columns((2,6))
            with title_container:
                with col1:
                    st.image("http://covers.openlibrary.org/b/ISBN/{}-M.jpg".format(books[books['Title']==N[i]]['ISBN'].values[0]))
                with col2:
                    st.header(N[i])
                    st.subheader(books[books['Title']==N[i]]['Author'].values[0])
                    st.text(books[books['Title']==N[i]]['Blurb'].values[0])
            # print(N[i])
            # print(books[books['Title']==N[i]]['Author'].values[0])
            # print(books[books['Title']==N[i]]['ISBN'].values[0])
            # print(books[books['Title']==N[i]]['Blurb'].values[0])

    book_list=books["Title"].values
    selected_book=st.selectbox("Select your book",book_list)
    x = st.slider("Set the number of results", 1, 20, 1)
    
    if st.button("Show similar books"):
        get_name(selected_book,x)
    
if rad=="About":
    st.title("Contact Me")
    st.subheader("Soumyadeep Datta")
    st.write("[GitHub](https://github.com/SoumyadeepDatta)")
    st.write("[LinkedIn](https://www.linkedin.com/in/soumyadeep-datta-884090216/)")
    st.title("Disclaimer")
    st.write("[scikit-learn](https://scikit-learn.org/stable/)")
    st.write("[Open Library Covers API](https://openlibrary.org/dev/docs/api/covers)")
    st.write("[Dataset Link](https://www.kaggle.com/jdobrow/57000-books-with-metadata-and-blurbs)")
    st.write("I had to trim the daraset as [Heroku](https://www.heroku.com/) supports upto 500 mb slug size. So out of 57,000 books, only 15000 are available under this model. Also some of the book's cover aren't available at this moment.")
    
