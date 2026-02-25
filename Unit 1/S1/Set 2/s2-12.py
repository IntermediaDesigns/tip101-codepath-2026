# ------------------------------------------------
#  *                    Problem 12: Calculate Factorial
#
#    Write a function factorial() that takes in an integer n as a parameter and
#    returns its factorial. The factorial of a number is the product of all positive
#    integers less than or equal to that number.
#    Example: 5! = 5 * 4 * 3 * 2 * 1 = 120


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(3))

# Example Output: 6
#
# ------------------------------------------------
