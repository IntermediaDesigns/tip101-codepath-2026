# ------------------------------------------------
#  *                    Problem 4: Binary Substrings
#
#    Write a function binary_substrings_count() that takes in a string s representing
#    a binary number as a parameter. The function counts the number of substrings that:
#      - contain an equal number of 0s and 1s
#      - all 0s in the substring are grouped consecutively
#      - all 1s in the substring are grouped consecutively


def binary_substrings_count(s):
    pass


s = "00110011"
print(binary_substrings_count(s))
# Substrings: "0011", "01", "1100", "10", "0011", "01"

s2 = "10101"
print(binary_substrings_count(s2))
# Substrings: "10", "01", "10", "01"

s3 = "1111"
print(binary_substrings_count(s3))

# Example Output:
# 6
# 4
# 0
#
# ------------------------------------------------
