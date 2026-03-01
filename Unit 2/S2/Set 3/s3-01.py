# ------------------------------------------------
#  *                    Problem 1: Return Book
#
#    Write a function return_book() that accepts a string title and a dictionary
#    library as parameters. library maps book titles to the number of copies in stock.
#    The function should increment the quantity of title in library by 1. If title
#    is not in the library, add it and set quantity to 1.
#    Return the updated library dictionary.


def return_book(title, library):
    pass


library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)

# Example Output:
# {'The Hobbit': 2, '1984': 2, 'The Great Gatsby': 4}
# {'The Hobbit': 2, '1984': 1, 'The Great Gatsby': 4, 'The Giver': 1}
#
# ------------------------------------------------
