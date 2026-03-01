# ------------------------------------------------
#  *                    Problem 2: Remove Element
#
#    Given a list of integers nums and an integer val, remove all occurrences
#    of val in-place. The order of remaining elements may change.
#    Return k, the count of elements not equal to val.
#    The first k elements of nums should contain those non-val elements.

def remove_element(nums, val):
    pass


nums1 = [3, 2, 2, 3]
k1 = remove_element(nums1, 3)
print(k1, nums1[:k1])
# Expected Output: 2, [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
k2 = remove_element(nums2, 2)
print(k2, nums2[:k2])
# Expected Output: 5, [0, 1, 4, 0, 3] (any order of these 5 elements is fine)

# ------------------------------------------------
