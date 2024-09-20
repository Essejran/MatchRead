
import pandas as pd
import streamlit as st

# Load data function
# @st.cache_data
# import os with full path
import os

# path to the data folder
data_folder = os.path.join(os.path.dirname(__file__), "..", "data")

books_ratings_path = os.path.join(data_folder, "books_rated.csv")
books_users_ratings_path = os.path.join(data_folder, "books_users_ratings.csv")
raters_15plus = os.path.join(data_folder, "raters_15plus.csv")
streamlit_df_path = os.path.join(data_folder, "streamlit_df.csv")

def load_data():
    books_ratings = pd.read_csv(books_ratings_path, 
                                sep=";", encoding="utf-8-sig")
    books_users_ratings = pd.read_csv(books_users_ratings_path, 
                                      sep=";", encoding="utf-8-sig")
    raters_15plus = pd.read_csv(raters_15plus, 
                                sep=";", encoding="utf-8-sig")
    streamlit_df = pd.read_csv(streamlit_df_path, 
                                sep=";", encoding="utf-8-sig")
    return books_ratings, books_users_ratings, raters_15plus, streamlit_df
# print("To load the dataframes, run this line of code:")
# print('books_ratings, books_users_ratings, raters_15plus = load_data()')


