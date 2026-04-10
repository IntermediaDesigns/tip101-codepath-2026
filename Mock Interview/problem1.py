# Problem #1 - Find the Index of the First Occurrence in a String
# Write a function that, when given two strings, needle and haystack, returns the index of the first occurrence of needle in haystack, or returns -1 if needle is not part of haystack.
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1

# 28. Find the Index of the First Occurrence in a String
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#  Save
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#  Save


# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("leetcode", "leeto"))


