# ------------------------------------------------
#  *                    Problem 9: First Item
#
#    Write a function get_first() that takes in a list as a parameter and returns
#    the first item in the list. Return None if the list is empty.
#
#    Note: pass is a keyword that is used as a placeholder for future code.


def get_first(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[0]

# Write your solution here!
result = get_first([3, 1, 6, 7, 5])
print(result)

# Example Input: [3, 1, 6, 7, 5]
# Example Output: 3
#
# ------------------------------------------------
