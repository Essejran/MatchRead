
import pandas as pd

books_goodreads = pd.read_csv('../data/goodreads_detailed.csv', sep=',', header=0)
print("Goodreads dataset loaded successfully as books_goodreads")

books_big = pd.read_csv("../data/df_clean.csv", sep=";", encoding="utf-8", engine="python", na_filter=True)
ratings = pd.read_csv('../data/ratings.csv', sep=',', header=0)
users = pd.read_csv('../data/users.csv', sep=',', header=0)
print("Pandas dataframes (books_goodreads, books_big, book, users, ratings) loaded successfully")

# Cleaning the column names:
users.columns = users.columns.str.lower().str.replace('-', '_')
ratings.columns = ratings.columns.str.lower().str.replace('-', '_')
print("Columns in DataFrames 'users' and 'ratings' renamed")

books = books_big.copy()
print("You can use the DataFrames 'books' or 'books_big' - they are exactly the same (big) dataset")

print("loading books_ratings and books_users_ratings")
books_ratings = pd.read_csv("../data/books_rated.csv", sep=";", encoding="utf-8-sig")
books_users_ratings = pd.read_csv("../data/books_users_ratings.csv", sep=";", encoding="utf-8-sig")
raters_15plus = pd.read_csv("../data/raters_15plus.csv", sep=";", encoding="utf-8-sig")

print("Ready to go!")