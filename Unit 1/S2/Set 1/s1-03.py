# ------------------------------------------------
#  *                    Problem 3: Return Doubled List
#
#    Modify the function doubled() so that instead of printing the items,
#    it returns a new list of the doubled numbers.


def doubled(lst):
    doubledList = []
    for items in lst:
        doubledList.append(items * 2)
        
    return doubledList

lst = [1, 2, 3]
new_lst = doubled(lst)
print(new_lst)

# Example Output:
# [2, 4, 6]
#
# ------------------------------------------------
