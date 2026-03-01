# ------------------------------------------------
#  *                    Problem 12: Printing Linked List
#
#    Write a function print_linked_list() that takes in a head node as a
#    parameter and prints the linked list using " -> " to separate each node's
#    value.
#    Note: The "head" is the first node in the list, like lst[0] of a normal list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    pass


# Build input linked list: a -> b -> c -> d -> e
e = Node("e")
d = Node("d", e)
c = Node("c", d)
b = Node("b", c)
a = Node("a", b)

print_linked_list(a)

# Example Output:
# a -> b -> c -> d -> e
#
# ------------------------------------------------
