# ------------------------------------------------
#  *                    Problem 7: Best Book
#
#    Write a function highest_rated() that returns the book with the highest rating.
#    The function takes in a list of dictionaries named books as a parameter. Each
#    dictionary represents a book with "title", "author", and "rating" keys.
#    The function should return the dictionary for the book with the highest rating.


def highest_rated(books):
    pass


books = [
    {
        "title": "Tomorrow, and Tomorrow, and Tomorrow",
        "author": "Gabrielle Zevin",
        "rating": 4.18
    },
    {
        "title": "A Fortune For Your Disaster",
        "author": "Hanif Abdurraqib",
        "rating": 4.47
    },
    {
        "title": "The Seven Husbands of Evenlyn Hugo",
        "author": "Taylor Jenkins Reid",
        "rating": 4.40
    }
]
print(highest_rated(books))

# Example Output:
# {"title": "A Fortune For Your Disaster", "author": "Hanif Abdurraqib", "rating": 4.47}
#
# ------------------------------------------------
