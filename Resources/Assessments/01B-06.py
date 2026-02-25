# In Range

# Complete the 'in_range' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER min_val
#  3. INTEGER max_val

def in_range(nums, min_val, max_val):
    return [num for num in nums if min_val < num < max_val]

nums = [1, 2, 3, 4, 5]
min_val = 1
max_val = 5
print(in_range(nums, min_val, max_val))  # Output: [2, 3, 4]



# Example 1:

# Input: nums = [1, 2, 3, 4, 5], min_val = 1, max_val = 5
# Output: [2, 3, 4]

# Example 2:

# Input: nums = [8, 6, 4], min_val = 2, max_val = 10
# Output: [8, 6, 4]