# Count Negatives

# count_negatives should return the number of negative numbers in a given input list. For example, count_negatives([-1, 2, 3, 4, -5]) should return 2. One of the following implementations is correct. The rest have a bug. Choose the option that correctly implements count_negatives.

def count_negatives(lst):
    count = 0
    for num in lst:
        if num < 0:
            count += 1
    return count

