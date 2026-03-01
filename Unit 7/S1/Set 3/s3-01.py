# ------------------------------------------------
#  *                    Problem 1: In The Stars
#
#    A recursive function is a function that calls itself within the body of the function.
#
#    Step 1: Run the recursive function insert_stars() below.
#    Step 2: Create another function insert_stars_iterative() that produces the same
#            output without using recursion or the built-in join() method.
#
#    Compare your iterative solution to the recursive solution. What is similar? What is different?


def insert_stars(s):
    if len(s) <= 1:
        return s
    else:
        return s[0] + '*' + insert_stars(s[1:])


print(insert_stars('abc'))


def insert_stars_iterative(s):
    pass


# Example Output: a*b*c
#
# ------------------------------------------------
