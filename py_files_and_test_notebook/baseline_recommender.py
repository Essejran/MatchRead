import pandas as pd

# Recommendation function based on collaborative filtering
def recommender_baseline(books_ratings):
    recommendations = books_ratings.sort_values(by=['avg_rating', 'nr_ratings'],
                                                ascending=[False, False])
    top_10_recs = recommendations.head(10)
    return top_10_recs[['isbn', 'book_title', 'image_url_m']]