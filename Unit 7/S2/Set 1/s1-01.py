# ------------------------------------------------
#  *                    Problem 1: Neatly Nested
#
#    Given a string, return True if it is a nesting of zero or more pairs of parentheses.
#    Return False otherwise. A valid pair of parentheses is defined as ().
#    The input string will only contain the characters ( or ).
#
#    Your solution must be recursive.
#    Evaluate the time and space complexity of your solution.


def is_nested(s):
    if s == "":
        return True
    elif len(s) % 2 != 0:
        return False
    elif s[0] == "(" and s[-1] == ")":
        return is_nested(s[1:-1])
    else:
        return False


print(is_nested("(())"))


# Example Input: "(())"
# Example Output: True
# Time Complexity: O(n) where n is the length of the input string. We need to check each character in the string once.
# Space Complexity: O(n) in the worst case due to the recursive call stack. In the best case (when the string is empty), the space complexity is O(1).
# ------------------------------------------------
