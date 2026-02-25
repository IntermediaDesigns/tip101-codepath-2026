# ------------------------------------------------
#  *                    Problem 4: Sum of Two Integers
#
#    The following function returns the sum of two integers: a and b.
#    Use the sum() function to calculate the sum of 13 and 27. Then, use the
#    sum() function again to double the calculated sum and print the result to the console.
#
#    Note: Do not use any mathematical operators such as +, -, *, or / when solving this problem.


def sum(a, b):
    return a + b

# Write your solution here!
result = sum(13, 27)
doubled_result = sum(result, result)

print(doubled_result)


# Example Input: 13 and 27
# Example Output: 80
#
# ------------------------------------------------
