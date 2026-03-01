# ------------------------------------------------
#  *                    Problem 6: Reverse Sublist of a Linked List
#
#    Given the head of a linked list and indices m and n (1-based), reverse
#    the nodes between positions m and n inclusive. Return the head of the
#    modified list. Assume 0 <= m <= n <= length of list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_between(head, m, n):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1 -> 2 -> 3 -> 4 -> 5, reverse positions 2 to 5
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(to_string(n1))
new_head = reverse_between(n1, 2, 5)
print(to_string(new_head))

# Build: 1 -> 2 -> 3 -> 4 -> 5, reverse positions 2 to 4
m5 = Node(5)
m4 = Node(4, m5)
m3 = Node(3, m4)
m2 = Node(2, m3)
m1 = Node(1, m2)
print(to_string(reverse_between(m1, 2, 4)))

# Example Output:
# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> 5 -> 4 -> 3 -> 2
# 1 -> 4 -> 3 -> 2 -> 5
#
# ------------------------------------------------
