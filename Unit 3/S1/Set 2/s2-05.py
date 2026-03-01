# ------------------------------------------------
#  *                    Problem 5: String Compression
#
#    Write a function compress_string() that takes in a string my_str as a parameter
#    and performs basic string compression using counts of repeated characters.
#    For example, "aabcccccaaa" would become "a2b1c5a3".
#    If the compressed string is not smaller than the original, return the original string.
#    Assume the string only has alphabetic characters.


def compress_string(my_str):
    pass


my_str = "aaaaabbcccd"
compressed_str = compress_string(my_str)
print(compressed_str)

my_str2 = "abcde"
compressed_str2 = compress_string(my_str2)
print(compressed_str2)

# Example Output:
# a5b2c3d1
# abcde    (did not compress because "a1b1c1d1e1" is longer)
#
# ------------------------------------------------
