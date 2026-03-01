# ------------------------------------------------
#  *                    Problem 1: Counting Down
#
#    A recursive function is a function that calls itself within the body of the function.
#
#    Step 1: Run the recursive function countdown() below.
#    Step 2: Create another function countdown_iterative() that produces the same
#            output without using recursion.
#
#    Compare your iterative solution to the recursive solution. What is similar? What is different?


def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)


countdown(5)


def countdown_iterative(n):
    pass


# Example Output:
# 5
# 4
# 3
# 2
# 1
#
# ------------------------------------------------
