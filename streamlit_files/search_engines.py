import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from loading_datasets import load_data

### This version includes content warnings for flagged authors ###

def search_titles(query):
    books_ratings = load_data()[0]
    # turning titles into TD-IDF matrix 
    vectorizer = TfidfVectorizer()
    tdidf = vectorizer.fit_transform(books_ratings['mod_title'])
    
    processed_query = re.sub('[^a-zA-Z0-9]', ' ', query.lower())
    query_vector = vectorizer.transform([processed_query])
    
    similarity = cosine_similarity(query_vector, tdidf).flatten()
    indices = np.argsort(similarity)[-10:][::-1]

    results = books_ratings.iloc[indices].reset_index(drop=True).head(10)
    
    # Add content warnings for flagged authors
    problematic_authors = {
        'john grisham': 'Made problematic comments in 2014. Please make your own research for more information. TW: Child pornography',
        'james patterson': 'Made problematic comments in 2022. Please make your own research for more information.',
        'j k rowling': 'Made transphobic comments. Please make your own research for more information.',
        'nicholas sparks': 'Accused of promoting racism, homophobia and discrimination. Please make your own research for more information.',
        'piers anthony' : 'Inappropriate comments in his work. Please make your own research for more information. TW: Underage sexual relations'
    }
    
    # Iterate over the results and add warnings if the author is flagged
    results['content_warning'] = results['mod_author'].str.lower().map(problematic_authors).fillna('')

    return results


# search function based on authors:
def search_authors(query):
    
    books_ratings = load_data()[0]

    # turning authors into TD-IDF matrix 
    # => Term Frequency-Inverse Document Frequency

    vectorizer = TfidfVectorizer()
    tdidf = vectorizer.fit_transform(books_ratings['mod_author'])
 
    processed_query = re.sub('[^a-zA-Z0-9]', ' ', query.lower())
    query_vector = vectorizer.transform([processed_query])

    similarity = cosine_similarity(query_vector, tdidf).flatten()
    indices = np.argsort(similarity)[-10:][::-1]
    results = books_ratings.iloc[indices].reset_index(drop=True).head(10)

    # Add content warnings for flagged authors
    problematic_authors = {
        'john grisham': 'Made problematic comments in 2014. Please make your own research for more information. TW: Child pornography',
        'james patterson': 'Made problematic comments in 2022. Please make your own research for more information.',
        'j k rowling': 'Made transphobic comments. Please make your own research for more information.',
        'nicholas sparks': 'Accused of promoting racism, homophobia and discrimination. Please make your own research for more information.',
        'piers anthony' : 'Inappropriate comments in his work. Please make your own research for more information. TW: Underage sexual relations'
    }
    
    # Iterate over the results and add warnings if the author is flagged
    results['content_warning'] = results['mod_author'].str.lower().map(problematic_authors).fillna('')

    return results


# Search function based on combined columns:
def search_all(query):

    books_ratings = load_data()[0]

    # Fill NaN values with empty strings for 'annotations'
    books_ratings['annotations'] = books_ratings['annotations'].fillna('')

    # Combine relevant columns into one for the TF-IDF
    books_ratings['combined_features'] = (
        books_ratings['mod_title'] + ' ' +
        books_ratings['mod_author'] + ' ' +
        books_ratings['mod_publisher'] + ' ' +
        books_ratings['genre'].apply(lambda x: ' '.join(x)) + ' ' +
        books_ratings['year_of_publication'].astype(str) + ' ' +
        books_ratings['annotations']
    )

    # Create TF-IDF matrix on combined features
    vectorizer = TfidfVectorizer()
    tdidf = vectorizer.fit_transform(books_ratings['combined_features'])
    
    # Process the search query
    processed_query = re.sub('[^a-zA-Z0-9]', ' ', query.lower())
    query_vector = vectorizer.transform([processed_query])
    
    # Compute cosine similarity
    similarity = cosine_similarity(query_vector, tdidf).flatten()

    # Get the indices of the top 10 results, sorted by similarity
    top_indices = np.argsort(similarity)[-10:][::-1]
    
    # Get the top results
    results = books_ratings.iloc[top_indices].reset_index(drop=True).head(10)

    # Add content warnings for flagged authors
    problematic_authors = {
        'john grisham': 'Made problematic comments in 2014. Please make your own research for more information. TW: Child pornography',
        'james patterson': 'Made problematic comments in 2022. Please make your own research for more information.',
        'j k rowling': 'Made transphobic comments. Please make your own research for more information.',
        'nicholas sparks': 'Accused of promoting racism, homophobia and discrimination. Please make your own research for more information.',
        'piers anthony' : 'Inappropriate comments in his work. Please make your own research for more information. TW: Underage sexual relations'
    }
    
    # Iterate over the results and add warnings if the author is flagged
    results['content_warning'] = results['mod_author'].str.lower().map(problematic_authors).fillna('')
        
    return results