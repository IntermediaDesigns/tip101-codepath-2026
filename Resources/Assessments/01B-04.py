# Count Negatives

# There's a bug in the following function! count_negatives should return the number of negative numbers in a given input list. For example, if we passed in [-1,2,3,4,-5]. count_negatives should return 2.

# Which of the following options describes the cause of the bug?

# Pick ONE option

# Replace count += 1 with count += num
# count = 0 should be replaced with count = lst[0]
# return count should be replaced with print(count) so the output is logged to the console.
# Currently, 0 will be counted as a negative number. if num <= 0 should be replaced with if num < 0

# Correct answer: Currently, 0 will be counted as a negative number. if num <= 0 should be replaced with if num < 0

def count_negatives(lst):
    count = 0
    for num in lst:
        if num < 0:
            count += 1
    return count

print(count_negatives([-1, 2, 3, 4, -5]))  # Should print 2
