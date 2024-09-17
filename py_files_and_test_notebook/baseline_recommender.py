import pandas as pd
from loading_datasets import load_data

# Recommendation function based on collaborative filtering
def recommender_baseline():
    books_ratings = load_data()[0]
    recommendations = books_ratings.sort_values(by=['avg_rating', 'nr_ratings'],
                                                ascending=[False, False])
    top_10_recs = recommendations.head(10)
    return top_10_recs[['isbn', 'book_title', 'image_url_m']]
