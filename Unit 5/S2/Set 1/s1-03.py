# ------------------------------------------------
#  *                    Problem 3: Add First
#
#    Write a function add_first() that takes in the head of a linked list and
#    a new_node from the Node class as parameters. Insert new_node as the new
#    head of the linked list and return new_node.
#    Note: The "head" is the first element, like lst[0] of a normal list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_first(head, new_node):
    pass


# Build linked list: Jigglypuff -> Wigglytuff
node_2 = Node("Wigglytuff")
node_1 = Node("Jigglypuff", node_2)

print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

# Example Output:
# Jigglypuff -> Wigglytuff
# Ditto -> Jigglypuff
#
# ------------------------------------------------
