# ------------------------------------------------
#  *                    Problem 6: Roman to Integer
#
#    Roman numerals are represented by seven symbols: I, V, X, L, C, D, M
#    with values: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
#
#    Numerals are usually written largest to smallest left to right. However,
#    subtraction is used in six cases:
#      I before V (5) or X (10) → 4 or 9
#      X before L (50) or C (100) → 40 or 90
#      C before D (500) or M (1000) → 400 or 900
#
#    Write a function roman_to_int() that takes in a string s representing a Roman
#    numeral and returns its integer value.


def roman_to_int(s):
    pass


s = "XL"
print(roman_to_int(s))

s2 = "LVIII"
print(roman_to_int(s2))

s3 = "MCMXCIV"
print(roman_to_int(s3))

# Example Output:
# 40
# 58
# 1994
#
# ------------------------------------------------
