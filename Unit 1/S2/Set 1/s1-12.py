# ------------------------------------------------
#  *                    Problem 12: Linear Search
#
#    Write a function linear_search() that takes in a list lst and a value target
#    as parameters. The function returns the index of target in lst if found.
#    If target is not found in lst, return -1.


def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


lst = [1, 4, 5, 2, 8]
position = linear_search(lst, 5)
print(position)

position = linear_search(lst, 10)
print(position)

# Example Output:
# 2
# -1
#
# ------------------------------------------------



