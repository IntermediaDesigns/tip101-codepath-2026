# ------------------------------------------------
#  *                    Problem 7: Best Movie Genre
#
#    Write a function most_popular_genre() that returns the genre with the highest
#    average rating across all movies. The function takes in a list of dictionaries
#    named movies, each with "title", "genre", and "rating" keys. The function
#    calculates the average rating for each genre and returns the genre with the
#    highest average rating.


def most_popular_genre(movies):
    pass


movies = [
    {"title": "Inception", "genre": "Science Fiction", "rating": 8.8},
    {"title": "The Matrix", "genre": "Science Fiction", "rating": 8.7},
    {"title": "Pride and Prejudice", "genre": "Romance", "rating": 7.8},
    {"title": "Sense and Sensibility", "genre": "Romance", "rating": 7.7}
]
print(most_popular_genre(movies))

# Example Output: Science Fiction
#
# ------------------------------------------------
