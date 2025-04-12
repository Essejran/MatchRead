import streamlit as st
from collab_filtering_recommender import recommender_cf
from loading_datasets import load_data
from baseline_recommender import recommender_baseline


# load the data
@st.cache_data
def load_data_cached():
    return load_data()

@st.cache_data
def recommender_bl_cached(baseline_df):
    return recommender_baseline(baseline_df)

@st.cache_data
def recommender_cf_cached(liked_books_isbn, data):
    return recommender_cf(liked_books_isbn, data)


baseline_df,_,_,data = load_data_cached()

basic_recs = recommender_bl_cached(baseline_df)

# Streamlit app
st.title("MatchRead - Hybrid Book Recommender")

# Multiselect widget with combined title and author as options
liked_books = st.multiselect(
    'Liked Books',
    options = data['title_author'].unique()
)

if st.button('Get Recommendations'):
    if liked_books == []:
        st.write("Add some books to get personalized recommendations.")

    else: 
        liked_books_isbn = data.isbn[data['title_author'].isin(liked_books)]
        liked_books_isbn = liked_books_isbn.unique().tolist()
        recommendations = recommender_cf_cached(liked_books_isbn, data)
        # Debugging: Check if recommendations are being returned
        if not recommendations.empty:
            st.write("Recommended Books:") 
            for _, row in recommendations.head(10).iterrows():
                st.image(row['image_url_m'], width=100)
                st.write(f"**{row['book_title']}**")
        else:
            st.write("We're still getting to know you, here's our best bet:")

for _, row in basic_recs.head(10).iterrows():
                st.image(row['image_url_m'], width=100)
                st.write(f"**{row['book_title']}**")




    