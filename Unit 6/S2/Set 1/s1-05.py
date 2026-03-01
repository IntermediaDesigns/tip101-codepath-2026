# ------------------------------------------------
#  *                    Problem 5: Add Two Numbers Represented by Linked Lists
#
#    Given two non-empty linked lists representing non-negative integers stored
#    in reverse order (each node is a single digit), add the two numbers and
#    return the sum as a linked list (also in reverse order).


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_two_numbers(head_a, head_b):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# List 1: 2 -> 4 -> 3  (represents 342)
# List 2: 5 -> 6 -> 4  (represents 465)
# 342 + 465 = 807, so result is 7 -> 0 -> 8
a3 = Node(3)
a2 = Node(4, a3)
a1 = Node(2, a2)

b3 = Node(4)
b2 = Node(6, b3)
b1 = Node(5, b2)

result = add_two_numbers(a1, b1)
print(to_string(result))

# List 1: 9 -> 9  (represents 99)
# List 2: 1       (represents 1)
# 99 + 1 = 100, so result is 0 -> 0 -> 1
c2 = Node(9, Node(9))
d1 = Node(1)
print(to_string(add_two_numbers(c2, d1)))

# Example Output:
# 7 -> 0 -> 8
# 0 -> 0 -> 1
#
# ------------------------------------------------
