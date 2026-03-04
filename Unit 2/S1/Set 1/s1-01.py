# ------------------------------------------------
#  *                    Problem 1: All In
#
#    Write a function all_in() that takes in a list of integers a and a list of
#    integers b as parameters. Given these two lists, return True if every element
#    in list a is in list b. Return False otherwise.


def all_in(a, b):
    
# Loop through each element in list a and check if it is in list b
    for items in a:
# Check if in list b
        if items not in b:
# If its not in b then return False
            return False
# if its true then return True
    return True


lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))

# Example Output:
# True
# False
#
# ------------------------------------------------

