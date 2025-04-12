import streamlit as st

# Recommendation function based on collaborative filtering
@st.cache_data
def recommender_baseline(baseline_df):
    recommendations = baseline_df.sort_values(by=['avg_rating', 'nr_ratings'],
                                                ascending=[False, False])
    top_10_recs = recommendations.head(10)
    return top_10_recs[['isbn', 'book_title', 'image_url_m', 'avg_rating', 'nr_ratings']]
