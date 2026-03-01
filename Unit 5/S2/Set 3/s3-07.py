# ------------------------------------------------
#  *                    Problem 7: Remove Node by Value from Linked List
#
#    Write a function ll_remove() that takes in the head of a linked list and
#    a value val as parameters. Remove the first node found with value val and
#    return the head of the linked list. If no node has value val, return the
#    list unchanged.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def ll_remove(head, val):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 5 -> 6 -> 7 -> 8
n4 = Node(8)
n3 = Node(7, n4)
n2 = Node(6, n3)
n1 = Node(5, n2)

print(to_string(n1))
head = ll_remove(n1, 6)
print(to_string(head))

# Example Output:
# 5 -> 6 -> 7 -> 8
# 5 -> 7 -> 8
#
# ------------------------------------------------
