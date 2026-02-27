# ------------------------------------------------
#  *                    Problem 8: Multiples of Five
#
#    Write a function multiples_of_five() that prints out multiples of 5
#    between 1 and 100 (inclusive).


def multiples_of_five():
    for i in range(1, 101): # add 1 to 101 because the range function does not include the end value
        if i % 5 == 0:
            print(i)


multiples_of_five() # call the function to print the multiples of 5

# Example Output:
# 5
# 10
# 15
# 20
# 25
# ....
# 90
# 95
# 100
#
# ------------------------------------------------
