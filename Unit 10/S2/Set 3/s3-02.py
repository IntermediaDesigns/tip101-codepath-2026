# ------------------------------------------------
#  *                    Problem 2: Intersection of Two Linked Lists
#
#    Given the heads of two singly linked lists, return the node at which
#    the two lists intersect. If they do not intersect, return None.
#    You may not modify either linked list.

class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def find_intersection(headA, headB):
    pass


# Example: Lists A and B share a tail starting at node c1
# A: a1 -> a2 -> c1 -> c2 -> c3
# B: b1 -> b2 -> b3 -> c1 -> c2 -> c3

c1 = Node(1)
c2 = Node(2)
c3 = Node(3)
c1.next = c2
c2.next = c3

a1 = Node(10, Node(20, c1))   # a1 -> a2 -> c1 -> c2 -> c3
b1 = Node(30, Node(40, Node(50, c1)))  # b1 -> b2 -> b3 -> c1 -> c2 -> c3

result = find_intersection(a1, b1)
print(result.val if result else None)  # Expected Output: 1 (the value of c1)

# Non-intersecting example
x1 = Node(1, Node(2))
y1 = Node(3, Node(4))
print(find_intersection(x1, y1))  # Expected Output: None

# ------------------------------------------------
