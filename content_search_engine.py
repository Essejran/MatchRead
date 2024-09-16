
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

################## IMPORTING DATASETS #########################################

# Load data function
def load_data():
    books_ratings = pd.read_csv("data/books_rated.csv", 
                                sep=";", encoding="utf-8-sig")
    books_users_ratings = pd.read_csv("data/books_users_ratings.csv", 
                                      sep=";", encoding="utf-8-sig")
    raters_15plus = pd.read_csv("data/raters_15plus.csv", 
                                sep=";", encoding="utf-8-sig")
    return books_ratings, books_users_ratings, raters_15plus

###############################################################################

# Search function based on content (content-based filtering)
def search_books(query, raters_15plus):

    # turning titles into TD-IDF matrix 
    # => Term Frequency-Inverse Document Frequency

    vectorizer = TfidfVectorizer()
    tdidf = vectorizer.fit_transform(raters_15plus['mod_titles'])
    ###
    processed_query = re.sub('[^a-zA-Z0-9]', ' ', query.lower())
    query_vector = vectorizer.transform([processed_query])
    
    similarity = cosine_similarity(query_vector, tdidf).flatten()
    indices = np.argpartition(similarity, -10)[-10:]
    
    results = raters_15plus.iloc[indices]
    results = results.sort_values(by='nr_ratings', ascending=False)
    
    return results.head(10)

#################### TESTING SECTION ##########################################
if __name__ == "__main__":
    # Step 1: Load the datasets
    books_ratings, books_users_ratings, raters_15plus = load_data()
    
    # Step 2: Testing the search_books function
    print("\nTesting content-based search_books function:")
    test_query = "Harry Potter"  # Simulate a user input for the search query
    search_results = search_books(test_query, raters_15plus)
    print("Search Results:\n", search_results)
###############################################################################