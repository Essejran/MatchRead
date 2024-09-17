import pandas as pd

# Recommendation function based on completely random sampling
def recommender_random(books_ratings, num_recommendations=10):
    """
    Get a specified number of random book recommendations from the DataFrame.
    
    Parameters:
    - books_ratings (pd.DataFrame): The DataFrame containing book data.
    - num_recommendations (int): The number of random book recommendations to generate. Default is 20.
    
    Returns:
    - pd.DataFrame: A DataFrame containing the randomly selected book recommendations.
    """
    # Ensure that the number of recommendations does not exceed the number of available books
    num_recommendations = min(num_recommendations, len(books_ratings))
    
    # Select random books from the DataFrame
    random_books = books_ratings.sample(n=num_recommendations)  # random_state ensures reproducibility
    
    return random_books

