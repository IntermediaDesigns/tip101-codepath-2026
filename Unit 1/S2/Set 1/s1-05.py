# ------------------------------------------------
#  *                    Problem 5: Max Difference
#
#    Write a function max_difference() that takes in a list of integers lst and
#    returns the difference between the smallest and largest value in the list.


def max_difference(lst):
    maxValue = lst[0]
    minValue = lst[0]
    
    for items in lst:
        if items > maxValue:
            maxValue = items
        elif items < minValue:
            minValue = items
            
    return maxValue - minValue


lst = [5, 22, 8, 10, 2]
max_diff = max_difference(lst)
print(max_diff)

# Example Output: 20
#
# ------------------------------------------------
