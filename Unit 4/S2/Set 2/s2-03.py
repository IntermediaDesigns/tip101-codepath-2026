# ------------------------------------------------
#  *                    Problem 3: Evaluate Palindrome
#
#    The is_palindrome() problem can also be solved without the two-pointer
#    technique. Evaluate the time and space complexity of your two-pointer
#    solution, then evaluate the alternative solution below.
#
#    Which has better time complexity?
#    Which has better space complexity?


def is_palindrome_two_pointer(s):
    pass  # Your two-pointer solution from s2-02.py goes here


def is_palindrome_slice(s):
    # Alternative solution
    reverse = s[::-1]
    return reverse == s


s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome_two_pointer(s))
print(is_palindrome_two_pointer(s2))
print(is_palindrome_slice(s))
print(is_palindrome_slice(s2))

# Example Output:
# True
# False
# True
# False
#
# ------------------------------------------------
