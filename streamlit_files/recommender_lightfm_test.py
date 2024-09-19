import streamlit as st
import joblib
import numpy as np
import pandas as pd
from lightfm import LightFM
from lightfm.data import Dataset
from loading_datasets import load_data

# Load the dataset
books_users_ratings = load_data()[1]

# Convert 'user_id', 'isbn', and 'year_of_publication' to strings
books_users_ratings['user_id'] = books_users_ratings['user_id'].astype(int).astype(str)
books_users_ratings['isbn'] = books_users_ratings['isbn'].astype(str)
books_users_ratings['year_of_publication'] = books_users_ratings['year_of_publication'].astype(str)

# Load the model
model = joblib.load('lightfm_model.pkl')

# Create a LightFM dataset object
dataset = Dataset()

# Fit the dataset to include all unique users and items
dataset.fit(
    users=books_users_ratings['user_id'].unique(),
    items=books_users_ratings['isbn'].unique()
)

# Build the interaction matrix with user-item pairs
interactions = dataset.build_interactions(
    [(str(x[0]), str(x[1])) for x in books_users_ratings[['user_id', 'isbn']].values]
)

# Create weights array from individual ratings
interaction_tuples = [(str(x[0]), str(x[1])) for x in books_users_ratings[['user_id', 'isbn']].values]
weights = np.array([books_users_ratings.loc[
    (books_users_ratings['user_id'] == u) & 
    (books_users_ratings['isbn'] == i), 
    'individual_rating'
].values[0] for u, i in interaction_tuples])

# Get the user and item mappings
user_mapping, _, item_mapping, _ = dataset.mapping()

####################
def recommend_books(model, interactions, user_id, user_mapping, item_mapping, num_recommendations=10):
    user_id = str(user_id)
    
    if user_id not in user_mapping:
        raise ValueError(f"User ID {user_id} is not found in the dataset.")
    
    user_idx = user_mapping[user_id]
    scores = model.predict(user_idx, np.arange(interactions.shape[1]))
    top_items = np.argsort(-scores)[:num_recommendations]
    recommended_isbns = [list(item_mapping.keys())[list(item_mapping.values()).index(item)] for item in top_items]
    
    return recommended_isbns
####################

# Streamlit app
st.title("Book Recommender System")

user_id = st.text_input("Enter User ID:")

if user_id:
    try:
        isbn_list = recommend_books(model, interactions, user_id, user_mapping, item_mapping)
        cols = ['book_title', 'book_author', 'year_of_publication', 'publisher']
        recommendations = books_users_ratings[books_users_ratings['isbn'].isin(isbn_list)]
        recommendations = recommendations[cols]
        st.write("Top Recommendations Using The LightFM Model:")
        st.write(recommendations)
    except ValueError as e:
        st.error(str(e))
