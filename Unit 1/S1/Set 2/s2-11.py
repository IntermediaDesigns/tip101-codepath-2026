# ------------------------------------------------
#  *                    Problem 11: Length of List
#
#    Without using the built-in len() function, write a function list_length()
#    that takes in a list lst as a parameter and returns the length of the list.


def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


lst = [2, 4, 6, 8, 10]
length = list_length(lst)
print(length)

# Example Output: 5
#
# ------------------------------------------------
