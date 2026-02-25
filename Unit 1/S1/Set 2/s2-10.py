# ------------------------------------------------
#  *                    Problem 10: Calculate Power
#
#    Write a function power() that takes in two integers base and exponent.
#    The function should return the value of the base number to the power of the exponent.


def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


pow1 = power(2, 5)
print(pow1)

pow2 = power(3, 3)
print(pow2)

# Example Output:
# 32
# 27
#
# ------------------------------------------------
