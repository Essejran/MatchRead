
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

############### FLAGGING CRITICAL AUTHORS #####################################

# Create a dictionary of authors and their problematic behavior
problematic_authors = {
    'john grisham': 'Made problematic comments in 2014. Please make your own research for more information. TW: Child pornography',
    'james patterson': 'Made problematic comments in 2022. Please make your own research for more information.',
    'j k rowling': 'Made transphobic comments. Please make your own research for more information.',
    'nicholas sparks': 'Accused of promoting racism, homophobia and discrimination. please make your own research for more information.',
    'piers anthony' : 'Inappropriate comments in his work. Please make your own research for more information. TW: Underage sexual relations'
}

# Create a new column with problematic messages
books_users_ratings['problematic_author'] = books_users_ratings['book_author'].apply(
    lambda author: problematic_authors.get(author, '')
)

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

    # Step 7: Loop through the results and add problematic author descriptions if applicable
    for index, row in results.iterrows():
        book_title = row['mod_titles']
        author = row['book_author']
        # rating = row['book_rating']
        rating_count = row['nr_ratings']
        
        # Print the book details
        print(f"Book: {book_title} by {author}")
        # print(f"Rating: {rating}, Number of Ratings: {rating_count}")
        
        # Check if the author is flagged as problematic and print the message if applicable
        if author in problematic_authors:
            print(f"⚠️ {problematic_authors[author]}")
        
        print() 
    
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