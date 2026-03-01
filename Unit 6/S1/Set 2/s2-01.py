# ------------------------------------------------
#  *                    Problem 1: One to Many
#
#    The single assignment statement below creates the linked list
#    Mario -> Luigi -> Wario. Break it apart into multiple lines with one call
#    to the Node constructor per line to recreate the same list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Original single-line version (do not modify):
# head = Node("Mario", Node("Luigi", Node("Wario")))

# Recreate the same list using multiple lines, one Node constructor per line:
head = None   # Replace with your multi-line solution


# Verify:
print(head.value, "->", head.next.value, "->", head.next.next.value)
print(head.next.next.next)

# Example Output:
# Mario -> Luigi -> Wario
# None
#
# ------------------------------------------------
