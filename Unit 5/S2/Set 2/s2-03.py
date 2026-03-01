# ------------------------------------------------
#  *                    Problem 3: Insert Value First
#
#    Write a function add_first() that takes in the head of a linked list and
#    a value val as parameters. Insert a new Node with value val as the new
#    head of the linked list and return the new node.
#    Note: The "head" is the first element, like lst[0] of a normal list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_first(head, val):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: A -> B -> C
node_c = Node("C")
node_b = Node("B", node_c)
node_a = Node("A", node_b)

print(to_string(node_a))
new_list = add_first(node_a, 0)
print(to_string(new_list))

# Example Output:
# A -> B -> C
# 0 -> A -> B -> C
#
# ------------------------------------------------
