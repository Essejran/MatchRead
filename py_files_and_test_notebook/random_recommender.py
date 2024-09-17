import pandas as pd
from loading_datasets import load_data

# Recommendation function based on completely random sampling
def recommender_random(num_recommendations=10):

    # Load the dataset needed (books_ratings):
    df = load_data()[0]

    # Ensure that the number of recommendations 
    # does not exceed the number of available books:
    num_recommendations = min(num_recommendations, len(df))

    # Select random books from the DataFrame
    random_books = df.sample(n=num_recommendations)
    
    return random_books[['isbn', 'book_title', 'image_url_m']]

