# Contains Duplicate

# Given an integer list nums, return True if any value appears at least twice in the list, and return False if every element is distinct.abs

# Example 1:
Input: [1, 2, 3, 1]
output: True

# Example 2:
Input: [1, 2, 3, 4]
output: False

# . 1 Using a Set to Track Seen Numbers
# 2. Iterate Through the List
# 3. Check for Duplicates
# 4. Return the Result

def contains_duplicate(nums): # Define a function that takes a list of numbers as input
    num_set = set() # Create an empty set to keep track of numbers we've seen so far

    for num in nums: # Loop through each number in the input list
        if num in num_set: # If the number is already in the set, we've found a duplicate
            return True
        num_set.add(num) # If the number is not in the set, add it to the set
    return False


print(contains_duplicate([1, 2, 3, 1]))  # Should print True
print(contains_duplicate([1, 2, 3, 4]))  # Should print False
