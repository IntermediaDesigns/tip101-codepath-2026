# ------------------------------------------------
#  *                    Problem 13: Calculate the Squares
#
#    Write a function squares() that takes a list of integers nums as a parameter
#    and returns a new list containing the square of each number in the original list.


def squares(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result

nums = [1, 2, 3, 4]
squared_nums = squares(nums)
print(squared_nums)


# Example Input: [1, 2, 3, 4]
# Example Output: [1, 4, 9, 16]
#
# ------------------------------------------------
