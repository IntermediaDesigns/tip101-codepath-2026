# ------------------------------------------------
#  *                    Problem 1: Nested Constructors
#
#    Using the Node class below, add a single line of code (outside the class)
#    that creates the linked list 4 -> 3 -> 2 using nested constructor calls
#    in one assignment statement.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Create the linked list 4 -> 3 -> 2 in a single line here
head = None  # Replace with your nested constructor call

# Verify:
print(head.value, "->", head.next.value, "->", head.next.next.value)

# Example Output:
# 4 -> 3 -> 2
#
# ------------------------------------------------
