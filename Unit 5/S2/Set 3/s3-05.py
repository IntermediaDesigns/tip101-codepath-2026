# ------------------------------------------------
#  *                    Problem 5: Copy Linked List
#
#    Write a function copy_ll() that takes in the head of a linked list and
#    creates a complete copy of it. Return the head of the new linked list.
#    The copy must not share any node objects with the original.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def copy_ll(head):
    pass


# Build: 5 -> 6 -> 7
n3 = Node(7)
n2 = Node(6, n3)
n1 = Node(5, n2)
head = n1

copy = copy_ll(head)
print(head.value, copy.value)

# Change original — should NOT affect the copy
head.value = 10
print(head.value, copy.value)

# Example Output:
# 5 5
# 10 5
#
# ------------------------------------------------
