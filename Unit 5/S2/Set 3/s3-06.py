# ------------------------------------------------
#  *                    Problem 6: Find Minimum in Linked List
#
#    Write a function find_min() that takes in the head of a linked list and
#    returns the minimum value. You can assume all node values are numeric.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_min(head):
    pass


# Build: 5 -> 6 -> 7 -> 8
n4 = Node(8)
n3 = Node(7, n4)
n2 = Node(6, n3)
n1 = Node(5, n2)
print(find_min(n1))

# Build: 8 -> 5 -> 6 -> 7
m4 = Node(7)
m3 = Node(6, m4)
m2 = Node(5, m3)
m1 = Node(8, m2)
print(find_min(m1))

# Example Output:
# 5
# 5
#
# ------------------------------------------------
