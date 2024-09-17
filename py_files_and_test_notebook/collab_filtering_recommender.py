
import pandas as pd
from loading_datasets import load_data

# Recommendation function based on collaborative filtering
def recommender_cf(liked_books):
    books_users_ratings = load_data()[1]
    # Create data frame of unique users who like the same books as user
    filtered_ratings = books_users_ratings[books_users_ratings['isbn'].
                                           isin(liked_books) & 
                                           (books_users_ratings[
                                               'individual_rating'] > 8)]
    overlap_users = set()
    # Remove duplicated rows (if any) where book-user-rating are all identical
    # Keep only the columns 'user_id', 'isbn', 'book_title', 'individual_rating'
    overlap_users = set(filtered_ratings.apply(
        lambda row: (row['user_id'], row['isbn'],
                     row['book_title'], row['individual_rating']), axis=1))
    overlap_users = pd.DataFrame(list(overlap_users), 
                                 columns=['user_id', 'isbn', 
                                          'book_title', 'individual_rating'])
    overlap_users['isbn'] = overlap_users['isbn'].astype(str)

    # overlap_users contains these users' ratings of OUR liked_books
    # now we need to add all the OTHER books they liked (rating > 8)
    # and remove all our liked_books to get fresh recommendations

    total_books = books_users_ratings[books_users_ratings['user_id']
                                      .isin(overlap_users['user_id'])]
                                        # All the books they've rated
    total_books = total_books[total_books['individual_rating'] > 8]
                                        # All the books they liked
    recommended = total_books[~total_books['isbn'].isin(liked_books)]
                                        # Only new books to our user
    recommended = recommended.drop_duplicates(subset='isbn') # dedupl. books
    recommended_2 = recommended['isbn'].value_counts().head(10).reset_index()
                                        # 10 books that were most often
                                        # rated > 8 by overlapping users
                                        # each row 1 indiv. rating > 8
                                        # of all the other books they like
    recommended_2.columns = ['isbn', 'count']
    recommended_with_titles = pd.merge(recommended_2, 
                                       total_books[['isbn', 'book_title', 
                                                    'image_url_m']], 
                                                    on='isbn', how='left')
    return recommended_with_titles[['isbn', 'book_title', 'image_url_m']]