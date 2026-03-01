# ------------------------------------------------
#  *                    Problem 6: How Many Smaller
#
#    Write a function smaller_numbers_than_current() that takes in a list of numbers
#    nums as a parameter. For each nums[i], find how many numbers in the list are
#    smaller than it (count all valid j's such that j != i and nums[j] < nums[i]).
#    Return the answers in a list.


def smaller_numbers_than_current(nums):
    pass


nums = [6, 1, 2, 2, 3]
print(smaller_numbers_than_current(nums))

# Explanation:
# nums[0] = 6 → four smaller numbers (1, 2, 2, 3) → ans[0] = 4
# nums[1] = 1 → no smaller numbers → ans[1] = 0
# nums[2] = 2 → one smaller number (1) → ans[2] = 1
# nums[3] = 2 → one smaller number (1) → ans[3] = 1
# nums[4] = 3 → three smaller numbers (1, 2, 2) → ans[4] = 3

# Example Output: [4, 0, 1, 1, 3]
#
# ------------------------------------------------
