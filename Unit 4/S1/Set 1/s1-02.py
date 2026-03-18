# ------------------------------------------------
#  *                    Problem 2: Two-Pointer Reverse List
#
#    Write a function reverse_list() that takes in a list lst and returns
#    elements of the list in reverse order. The list should be reversed in-place
#    without using list slicing (e.g. lst[::-1]). Instead, use the two-pointer
#    approach: initialize one pointer at the beginning and one at the end, then
#    shift them inward, swapping elements until they meet.


def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst


print(reverse_list([1, 2, 3, 4, 5]))

# Example Output:
# [5, 4, 3, 2, 1]
#
# ------------------------------------------------
