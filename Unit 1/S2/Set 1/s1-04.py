# ------------------------------------------------
#  *                    Problem 4: Flip Signs
#
#    Write a function flip_sign() that takes in a list of integers lst as a parameter
#    and returns a new list where each number in the original list has been multiplied by -1.


def flip_sign(lst):
    flippedList = []
    for items in lst:
        flippedList.append(items * -1)
        
    return flippedList


lst = [1, -2, -3, 4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

# Example Output:
# [-1, 2, 3, -4]
#
# ------------------------------------------------
