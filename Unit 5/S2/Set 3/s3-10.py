# ------------------------------------------------
#  *                    Problem 10: Find Length of Doubly Linked List from Any Node
#
#    Write a function get_length() that takes in a node at an unknown position
#    within a doubly linked list and returns the total length of the entire list.


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def get_length(node):
    pass


# Build DLL: 3 <-> 5 <-> 6 <-> 7
n4 = Node(7)
n3 = Node(6, n4)
n2 = Node(5, n3)
n1 = Node(3, n2)
n4.prev = n3
n3.prev = n2
n2.prev = n1

# Pass in the middle node (value=6)
print(get_length(n3))

# Example Output:
# 4
#
# ------------------------------------------------
