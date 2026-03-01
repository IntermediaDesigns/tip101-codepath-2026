# ------------------------------------------------
#  *                    Problem 1: Hello Hello
#
#    A recursive function is a function that calls itself within the body of the function.
#
#    Step 1: Run the recursive function repeat_hello() below.
#    Step 2: Create another function repeat_hello_iterative() that produces the same
#            output without using recursion.
#
#    Compare your iterative solution to the recursive solution. What is similar? What is different?


def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n - 1)


repeat_hello(5)


def repeat_hello_iterative(n):
    pass


# Example Output:
# Hello
# Hello
# Hello
# Hello
# Hello
#
# ------------------------------------------------
