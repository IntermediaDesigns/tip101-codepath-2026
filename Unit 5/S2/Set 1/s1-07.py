# ------------------------------------------------
#  *                    Problem 7: Insert Value
#
#    Write a function ll_insert() that takes in the head of a linked list, a
#    value val, and an index i as parameters. Insert a new Node with value val
#    at index i and return the head of the linked list.
#    If i is greater than the list length, insert at the end.
#    Hint: Linked lists don't have built-in indices — track them yourself.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def ll_insert(head, val, i):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 3 -> 8 -> 12 -> 9
n4 = Node(9)
n3 = Node(12, n4)
n2 = Node(8, n3)
n1 = Node(3, n2)
head = n1

print(to_string(head))
head = ll_insert(head, 20, 2)
print(to_string(head))

# Example Output:
# 3 -> 8 -> 12 -> 9
# 3 -> 8 -> 20 -> 12 -> 9
#
# ------------------------------------------------
