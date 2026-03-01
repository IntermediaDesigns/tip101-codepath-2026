# ------------------------------------------------
#  *                    Problem 6: Circular Linked List Delete
#
#    Given the head of a CIRCULAR linked list and a value val, delete the
#    first node with value val. Return the head of the modified list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delete_node(head, val):
    pass


def print_circular(head, steps=6):
    """Helper: print first `steps` nodes of a circular list to verify."""
    current = head
    output = []
    for _ in range(steps):
        output.append(str(current.value))
        current = current.next
    print(" -> ".join(output) + " -> ...")


# Example 1: Delete middle node (val=2)
num1 = Node(1); num2 = Node(2); num3 = Node(3)
num1.next = num2; num2.next = num3; num3.next = num1
head = delete_node(num1, 2)
print_circular(head)
# Expected: 1 -> 3 -> 1 -> 3 -> ...

# Example 2: Delete head node (val=1, new head should be 2)
num1 = Node(1); num2 = Node(2); num3 = Node(3)
num1.next = num2; num2.next = num3; num3.next = num1
head = delete_node(num1, 1)
print_circular(head)
# Expected: 2 -> 3 -> 2 -> 3 -> ...

# Example Output:
# 1 -> 3 -> 1 -> 3 -> 1 -> 3 -> ...
# 2 -> 3 -> 2 -> 3 -> 2 -> 3 -> ...
#
# ------------------------------------------------
