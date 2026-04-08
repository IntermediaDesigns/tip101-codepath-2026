# ------------------------------------------------
#  *                    Problem 2: Factorial Cases
#
#    Given the base case and recursive case, write a function factorial() that returns
#    the factorial of a non-negative integer n. The factorial of a number is the product
#    of all numbers between 1 and n.
#
#    Base Case: The factorial of 0 is 1.
#    Recursive Case: The factorial of n is n * the factorial of n-1.


def factorial(n):
    factorial_value = 1
    for i in range(1, n + 1):
        factorial_value *= i
    return factorial_value


print(factorial(5))



# Example Input: 5
# Example Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
#
# ------------------------------------------------
