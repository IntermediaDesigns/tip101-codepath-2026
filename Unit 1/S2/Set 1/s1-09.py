# ------------------------------------------------
#  *                    Problem 9: Divisors
#
#    Write a function find_divisors() that takes in an integer n as a parameter
#    and returns a list of all divisors of n.


def find_divisors(n):
    divisors = []
    for i in range(1, n + 1): # add 1 to n because the range function does not include the end value
        if n % i == 0:
            divisors.append(i)
            
    return divisors


lst = find_divisors(6)
print(lst)

# Example Output:
# [1, 2, 3, 6]
#
# ------------------------------------------------
