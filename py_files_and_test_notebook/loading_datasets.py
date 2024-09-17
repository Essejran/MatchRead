
import pandas as pd

# Load data function
def load_data():
    books_ratings = pd.read_csv("../data/books_rated.csv", 
                                sep=";", encoding="utf-8-sig")
    books_users_ratings = pd.read_csv("../data/books_users_ratings.csv", 
                                      sep=";", encoding="utf-8-sig")
    raters_15plus = pd.read_csv("../data/raters_15plus.csv", 
                                sep=";", encoding="utf-8-sig")
    return books_ratings, books_users_ratings, raters_15plus
# print("To load the dataframes, run this line of code:")
# print('books_ratings, books_users_ratings, raters_15plus = load_data()')


