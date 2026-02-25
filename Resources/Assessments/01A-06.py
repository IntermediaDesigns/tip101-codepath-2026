# List Minimum

# Without using the built-in function min, write.a function that finds the minimum value in a list of integers.

# Example:

# Input: [5,1,2,3,4]
# Output: 1

# Example 2:
# Input: [10,8,2,4,6]
# Output: 2

def find_min(lst):
    if not lst:
        return None  # Handle empty list case
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

print("Example 1:", find_min([5, 1, 2, 3, 4]))  # Output: 1
print("Example 2:", find_min([10, 8, 2, 4, 6]))  # Output: 2