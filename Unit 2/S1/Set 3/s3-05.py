# ------------------------------------------------
#  *                    Problem 5: Average Book Ratings
#
#    Write a function average_book_ratings() that calculates the average rating for
#    each book in a collection. The function takes one parameter: a dictionary
#    book_ratings where each key-value pair represents a book title and a list of
#    its ratings (as floats). The function returns a new dictionary with book titles
#    as keys and their average rating as values.


def average_book_ratings(book_ratings):
    pass


book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
print(average_book_ratings(book_ratings))

# Example Output:
# {'The Great Gatsby': 4.166666666666667, 'To Kill a Mockingbird': 4.675000000000001}
#
# ------------------------------------------------
