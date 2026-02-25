# ------------------------------------------------
#  *                    Problem 10: Last Item
#
#    Write a function get_last() that takes in a list as a parameter and returns
#    the last item in the list. Return None if the list is empty.


def get_last(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[-1]
    
# Write your solution here!
result = get_last([3, 1, 6, 7, 5])
print(result)


# Example Input: [3, 1, 6, 7, 5]
# Example Output: 5
#
# ------------------------------------------------
