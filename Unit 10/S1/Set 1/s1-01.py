# ------------------------------------------------
#  *                    Problem 1: Valid Parentheses
#
#    Given a string s containing just the characters '(', ')', '{', '}', '['
#    and ']', return True if the input string is valid and False otherwise.
#
#    An input string is valid if:
#    1. Open brackets must be closed by the same type of brackets.
#    2. Open brackets must be closed in the correct order.
#    3. Every close bracket has a corresponding open bracket of the same type.

def is_valid(s):
    pass


print(is_valid("()"))       # Expected Output: True
print(is_valid("()[]{}"))   # Expected Output: True
print(is_valid("(())"))     # Expected Output: True
print(is_valid("(]"))       # Expected Output: False
print(is_valid("([)]"))     # Expected Output: False

# ------------------------------------------------
