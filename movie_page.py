import pandas as pd
import streamlit as st

def show_movie_based_page():
	st.title("User Based Recommendation System")
	train_data = pd.read_csv("./Recommendation_data/train.csv")
	user_movie_matrix = train_data.pivot(index='uID', columns='mID', values='rating').fillna(0)
	movie_similarity = cosine_similarity(user_movie_matrix.T)
	movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

	def get_movie_based_recommendations(movie_id, movie_similarity_df, n_recommendations=None):
	    sim_scores = movie_similarity_df[movie_id]
	    sim_scores = sim_scores.sort_values(ascending=False)
	    top_movie_indices = sim_scores.iloc[1:n_recommendations+1].index
	    top_movie_titles = movies_data[movies_data['mID'].isin(top_movie_indices)]['title']
	    return top_movie_titles

	movie_id = st.number_input('Movie id', min_value=1)  
	recommendations = st.number_input('Number of Recommendations', min_value=1)  
	recommended_movies = recommended_movies = get_movie_based_recommendations(movie_id, movie_similarity_df,recommendations)
	st.write('Top Recommendations : ', recommended_movies)