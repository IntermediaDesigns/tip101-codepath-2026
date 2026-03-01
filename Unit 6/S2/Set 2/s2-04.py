# ------------------------------------------------
#  *                    Problem 4: Identical Linked Lists
#
#    Two linked lists are identical when they have the same values in the same
#    order. Given the heads of two linked lists, return True if they are
#    identical and False otherwise.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_identical(head_a, head_b):
    pass


# Example 1: 1->2->3->4 vs 1->2->3->4
a4 = Node(4); a3 = Node(3, a4); a2 = Node(2, a3); a1 = Node(1, a2)
b4 = Node(4); b3 = Node(3, b4); b2 = Node(2, b3); b1 = Node(1, b2)
print(is_identical(a1, b1))

# Example 2: 1->2->3->4 vs 1->3->4->2
c4 = Node(4); c3 = Node(3, c4); c2 = Node(2, c3); c1 = Node(1, c2)
d4 = Node(2); d3 = Node(4, d4); d2 = Node(3, d3); d1 = Node(1, d2)
print(is_identical(c1, d1))

# Example 3: different lengths 1->2->3 vs 1->2
e3 = Node(3); e2 = Node(2, e3); e1 = Node(1, e2)
f2 = Node(2); f1 = Node(1, f2)
print(is_identical(e1, f1))

# Example Output:
# True
# False
# False
#
# ------------------------------------------------
