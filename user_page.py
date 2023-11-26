import pandas as pd
import streamlit as st

def show_user_based_page():
	st.title("User Based Recommendation System")
	train_data = pd.read_csv("train.csv")
	user_movie_matrix = train_data.pivot(index='uID', columns='mID', values='rating').fillna(0)
	sparse_matrix = csr_matrix(user_movie_matrix.values)
	user_similarity = cosine_similarity(sparse_matrix)
	user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

	def get_user_based_recommendations(user_id, user_similarity_df, user_movie_matrix, n_recommendations=None):
	    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
	    similar_users_ratings = user_movie_matrix.loc[similar_users]
	    movie_recommendation_scores = similar_users_ratings.mean(axis=0)
	    movie_recommendations = movie_recommendation_scores.sort_values(ascending=False)
	    already_watched_indices = user_movie_matrix.loc[user_id].loc[user_movie_matrix.loc[user_id] > 0].index
	    movie_recommendations = movie_recommendations.loc[~movie_recommendations.index.isin(already_watched_indices)]
	    top_movie_recommendations = movie_recommendations.head(n_recommendations).index
	    top_movie_titles = movies_data[movies_data['mID'].isin(top_movie_recommendations)]['title']
	    return top_movie_titles

	user_id = st.number_input('User', min_value=1)  
	recommendations = st.number_input('Number of Recommendations', min_value=1)  
	recommended_movies = get_user_based_recommendations(user_id, user_similarity_df, user_movie_matrix,recommendations)
	st.write('Top Recommendations : ', recommended_movies)
