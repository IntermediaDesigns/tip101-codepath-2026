# ------------------------------------------------
#  *                    Problem 7: Good Pairs
#
#    Write a function num_identical_pairs() that takes in a list of integers nums and
#    returns the number of good pairs. A pair (i, j) is called good if
#    nums[i] == nums[j] and i < j.


def num_identical_pairs(nums):
    pass


nums = [1, 2, 3, 1, 1, 3]
print(num_identical_pairs(nums))
# Explanation: Good pairs → (0,3), (0,4), (2,5), (3,4) → count = 4

nums = [1, 2, 3]
print(num_identical_pairs(nums))
# Explanation: No identical pairs → count = 0

nums = [1, 1, 1, 1]
print(num_identical_pairs(nums))
# Explanation: Good pairs → (0,1),(0,2),(0,3),(1,2),(1,3),(2,3) → count = 6

# Example Output:
# 4
# 0
# 6
#
# ------------------------------------------------
