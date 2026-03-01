# ------------------------------------------------
#  *                    Problem 5: Partition Labels
#
#    Write a function partition_label() that takes in a string s of lowercase letters
#    as a parameter. The function partitions s into as many parts as possible so that
#    each unique letter appears in at most one part. Returns a list of integers
#    representing the size of these parts.


def partition_label(s):
    pass


s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))
# s1 partitioned into "ababcbaca", "defegde", "hijhklij"

s2 = "abcabcbadefffeda"
print(partition_label(s2))
# s2 cannot be partitioned further because of the "a" at the end

# Example Output:
# [9, 7, 8]
# [16]
#
# ------------------------------------------------
