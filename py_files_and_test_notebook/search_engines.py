import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Search function based on book titles:
def search_titles(query, raters_15plus):
    # turning titles into TD-IDF matrix 
    # => Term Frequency-Inverse Document Frequency

    vectorizer = TfidfVectorizer()
    tdidf = vectorizer.fit_transform(raters_15plus['mod_title'])
    ###
    processed_query = re.sub('[^a-zA-Z0-9]', ' ', query.lower())
    query_vector = vectorizer.transform([processed_query])
    
    similarity = cosine_similarity(query_vector, tdidf).flatten()
    indices = np.argpartition(similarity, -10)[-10:]
    
    results = raters_15plus.iloc[indices]
    results = results.sort_values(by='nr_ratings', ascending=False)
    
    return results.head(10)


# search function based on authors:
def search_authors(query, raters_15plus):
    # turning authors into TD-IDF matrix 
    # => Term Frequency-Inverse Document Frequency

    vectorizer = TfidfVectorizer()
    tdidf = vectorizer.fit_transform(raters_15plus['mod_author'])
 
    processed_query = re.sub('[^a-zA-Z0-9]', ' ', query.lower())
    query_vector = vectorizer.transform([processed_query])

    similarity = cosine_similarity(query_vector, tdidf).flatten()
    indices = np.argpartition(similarity, -10)[-10:]

    results = raters_15plus.iloc[indices]   
    results = results.sort_values(by='nr_ratings', ascending=False)

    return results.head(10)


# Search function based on combined columns:
def search_all(query, raters_15plus):

    # Fill NaN values with empty strings for 'annotations'
    raters_15plus['annotations'] = raters_15plus['annotations'].fillna('')

    # Combine relevant columns into one for the TF-IDF
    raters_15plus['combined_features'] = (
        raters_15plus['mod_title'] + ' ' +
        raters_15plus['mod_author'] + ' ' +
        raters_15plus['mod_publisher'] + ' ' +
        raters_15plus['genre'].apply(lambda x: ' '.join(x)) + ' ' +
        raters_15plus['year_of_publication'].astype(str) + ' ' +
        raters_15plus['annotations']
    )

    # Create TF-IDF matrix on combined features
    vectorizer = TfidfVectorizer()
    tdidf = vectorizer.fit_transform(raters_15plus['combined_features'])
    
    # Process the search query
    processed_query = re.sub('[^a-zA-Z0-9]', ' ', query.lower())
    query_vector = vectorizer.transform([processed_query])
    
    # Compute cosine similarity
    similarity = cosine_similarity(query_vector, tdidf).flatten()
    indices = np.argpartition(similarity, -10)[-10:]
    
    # Get the top results
    results = raters_15plus.iloc[indices]
    results = results.sort_values(by='nr_ratings', ascending=False)
    
    return results.head(10)

