# ------------------------------------------------
#  *                    Problem 8: Move Tail to Front of Linked List
#
#    Write a function tail_to_head() that takes in the head of a linked list
#    and moves the tail node to the front of the list. Return the new head.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def tail_to_head(head):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1 -> 2 -> 3 -> 4
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(to_string(n1))
head = tail_to_head(n1)
print(to_string(head))

# Example Output:
# 1 -> 2 -> 3 -> 4
# 4 -> 1 -> 2 -> 3
#
# ------------------------------------------------
