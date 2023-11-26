import streamlit as st
from user_page import show_user_based_page
from movie_page import show_movie_based_page

page = st.sidebar.selectbox("User Based Recommendation Or Movie Based Recommendation", ("User Based", "Movie Based"))

if page == "User Based":
    show_user_based_page()
else:
    show_movie_based_page()