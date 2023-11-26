import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

def show_movie_based_page():
    st.title("Movie Based Recommendation System")

    # Load data
    movies_data = pd.read_csv("movies.csv")
    train_data = pd.read_csv("train.csv")

    # Create movie similarity matrix
    user_movie_matrix = train_data.pivot(index='uID', columns='mID', values='rating').fillna(0)
    movie_similarity = cosine_similarity(user_movie_matrix.T)
    movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

    def get_movie_based_recommendations(movie_id, movie_similarity_df, n_recommendations=None):
        sim_scores = movie_similarity_df[movie_id]
        sim_scores = sim_scores.sort_values(ascending=False)
        top_movie_indices = sim_scores.iloc[1:n_recommendations+1].index
        top_movie_titles = movies_data[movies_data['mID'].isin(top_movie_indices)]['title']
        return top_movie_titles

    movielist = movies_data['title'].unique()
    moviename = st.selectbox("Movie Name", movielist)
    movienumber = movies_data[movies_data['title'] == moviename]['mID'].iloc[0]
    recommendations = st.number_input('Number of Recommendations', min_value=1)

    if st.button('Get Recommendations'):
        recommended_movies = get_movie_based_recommendations(movienumber, movie_similarity_df, recommendations)
        st.write('Top Recommendations:', recommended_movies.tolist())
