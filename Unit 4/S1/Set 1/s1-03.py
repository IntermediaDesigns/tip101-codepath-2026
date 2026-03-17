# ------------------------------------------------
#  *                    Problem 3: Evaluating Solutions
#
#    The reverse_list() problem can also be solved without the two-pointer
#    technique. Evaluate the time and space complexity of your two-pointer
#    solution, then evaluate the alternative solution below.
#
#    Which has better time complexity?
#    Which has better space complexity?


def reverse_list_two_pointer(lst):
    pass  # Your two-pointer solution from s1-02.py goes here


def reverse_list_slice(lst):
    # Alternative solution
    reversed_lst = lst[::-1]
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]
    return lst


lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]

print(reverse_list_two_pointer(lst1))
print(reverse_list_slice(lst2))

# Example Output:
# [5, 4, 3, 2, 1]
# [5, 4, 3, 2, 1]
#
# ------------------------------------------------
