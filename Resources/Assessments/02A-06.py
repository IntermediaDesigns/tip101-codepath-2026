# Element Frequency Greater than N

# Given a list of integers nums and an integer n. return a dictionary with elements as keys and their frequecies as values, but only include elements whose frequency is greater than n.abs

# Example 1:
# Input: nums = [1, 1, 2, 3, 3, 3, 4], n = 1
# Output: {1: 2, 3: 3}

# Example 2:
# Input: nums = [1, 2, 3, 4, 5], n = 0
# Output: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}

def frequency_greater_than_n(nums, n): # Define a function that takes a list of numbers and an integer n as input
    freq = {} # Create an empty dictionary to store the frequency of each element
    for num in nums: # Loop through each number in the input list
        freq[num] = freq.get(num, 0) + 1 # Update the frequency count for the current number
    # Filter the dictionary to include only elements with frequency greater than n
    return {key: value for key, value in freq.items() if value > n}

print(frequency_greater_than_n([1, 1, 2, 3, 3, 3, 4], 1))  # Should print {1: 2, 3: 3}
print(frequency_greater_than_n([1, 2, 3, 4, 5], 0))  # Should print {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}