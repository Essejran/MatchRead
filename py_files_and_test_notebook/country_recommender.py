import pandas as pd
from loading_datasets import load_data

# Recommendation function based on top rated books in a specific country:
def recommender_country(country="Germany"):
    df = load_data()[1]
    recommendations = df[df['country'] == country]
    recommendations = recommendations.sort_values(by=['avg_rating', 'nr_ratings'], ascending=[False, False])
    recommendations = recommendations.drop_duplicates(subset='isbn')
    recommendations = recommendations.head(10)
    return recommendations[['isbn', 'book_title', 'image_url_m']]