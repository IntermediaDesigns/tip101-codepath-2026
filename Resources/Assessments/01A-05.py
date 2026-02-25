# Find Sum

# Write a function that returns the sum of all the elements in a list.  Do not use the built-in sum function.

# Example 1:

# Input: [1,2,3,4,5]
# Output: 15

# Example 2:

# Input: [2,4,6,8,10]
# Output: 30

import math
import os
import random
import re
import sys


#
# Complete the 'find_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY lst as parameter.
#


def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

print("Example 1:", find_sum([1, 2, 3, 4, 5]))  # Output: 15
print("Example 2:", find_sum([2, 4, 6, 8, 10]))  # Output: 30


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    temp = input()

    if len(temp) > 70:
        input_string = temp
        chunks = input_string.split(", ")
        list_of_lists = [list(map(int, chunk.split())) for chunk in chunks]
        result = [find_sum(lst) for lst in list_of_lists]
    else:
        result = find_sum([int(n) for n in temp.split()])

    fptr.write(str(result) + "\n")

    fptr.close()
