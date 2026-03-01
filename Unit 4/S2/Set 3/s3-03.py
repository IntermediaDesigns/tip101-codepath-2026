# ------------------------------------------------
#  *                    Problem 3: Evaluate Two Sum
#
#    The two_sum() problem can also be solved without the two-pointer technique.
#    Evaluate the time and space complexity of your two-pointer solution, then
#    evaluate the alternative solution below.
#
#    Which has better time complexity?
#    Which has better space complexity?


def two_sum_two_pointer(nums, target):
    pass  # Your two-pointer solution from s3-02.py goes here


def two_sum_hashmap(nums, target):
    # Alternative solution
    prev_map = {}  # Value to index mapping
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i


nums = [2, 7, 11, 15, 17]

print(two_sum_two_pointer(nums, 9))
print(two_sum_two_pointer(nums, 18))
print(two_sum_hashmap(nums, 9))
print(two_sum_hashmap(nums, 18))

# Example Output:
# [0, 1]
# [1, 2]
# [0, 1]
# [1, 2]
#
# ------------------------------------------------
