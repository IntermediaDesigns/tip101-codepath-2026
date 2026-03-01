# ------------------------------------------------
#  *                    Problem 3: Delete Duplicates in a Linked List
#
#    Given the head of a SORTED linked list, delete all elements that occur
#    more than once in the list (remove ALL occurrences, not just the extras).
#    The resulting list should maintain sorted order. Return the head.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delete_dupes(head):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1 -> 2 -> 3 -> 3 -> 4 -> 5
n6 = Node(5)
n5 = Node(4, n6)
n4 = Node(3, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(to_string(n1))
print(to_string(delete_dupes(n1)))

# Build: 1 -> 1 -> 2 -> 3 -> 3
m5 = Node(3)
m4 = Node(3, m5)
m3 = Node(2, m4)
m2 = Node(1, m3)
m1 = Node(1, m2)
print(to_string(delete_dupes(m1)))

# Example Output:
# 1 -> 2 -> 3 -> 3 -> 4 -> 5
# 1 -> 2 -> 4 -> 5
# 2
#
# ------------------------------------------------
