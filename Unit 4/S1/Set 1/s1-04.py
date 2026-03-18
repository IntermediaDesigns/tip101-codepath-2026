# ------------------------------------------------
#  *                    Problem 4: Move Even Integers
#
#    Write a function sort_array_by_parity() that takes in an integer list nums
#    as a parameter and moves all the even integers to the beginning of the list
#    followed by all the odd integers. The function returns any list that
#    satisfies this condition.


def sort_array_by_parity(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if left < right and nums[left] % 2 == 0:
            left += 1
        if left < right and nums[right] % 2 != 0:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        
    return nums


nums = [3, 1, 2, 4]
nums2 = [0]

print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

# Example Output:
# [2, 4, 3, 1]  (also acceptable: [4,2,3,1], [2,4,1,3], [4,2,1,3])
# [0]
#
# ------------------------------------------------
