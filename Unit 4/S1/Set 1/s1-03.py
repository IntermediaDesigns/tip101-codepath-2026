# ------------------------------------------------
#  *                    Problem 3: Evaluating Solutions
#
#    The reverse_list() problem can also be solved without using the two pointer
#    technique (as you may have seen it in previous units)! Evaluate the time
#    and space complexity of your two-pointer solution.
#
#    Then, evaluate the time and space of the following solution:
#
#    def reverse_list(lst):
#        # Create a new reversed list
#        reversed_lst = lst[::-1]
#        # Copy the elements back into the original list
#        for i in range(len(lst)):
#            lst[i] = reversed_lst[i]
#
#    Which has better time complexity?
#    Which has better space complexity?
# ------------------------------------------------


def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]

print(reverse_list_two_pointer(lst1))
print(reverse_list_slice(lst2))

# Example Output:
# [5, 4, 3, 2, 1]
# [5, 4, 3, 2, 1]