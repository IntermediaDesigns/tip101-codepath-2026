# ------------------------------------------------
#  *                    Problem 3: Insert Node as Second Element
#
#    Write a function add_second() that takes in the head of a linked list and
#    a value val as parameters. Insert val as the second node in the linked
#    list and return the head. You can assume head is not None.
#    Note: The "head" is the first element, like lst[0] of a normal list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_second(head, val):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1 -> 3 -> 4
n3 = Node(4)
n2 = Node(3, n3)
n1 = Node(1, n2)

print(to_string(n1))
head = add_second(n1, 2)
print(to_string(head))

# Example Output:
# 1 -> 3 -> 4
# 1 -> 2 -> 3 -> 4
#
# ------------------------------------------------
