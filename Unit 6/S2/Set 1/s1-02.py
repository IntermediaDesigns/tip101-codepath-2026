# ------------------------------------------------
#  *                    Problem 2: Find Last Node in a Linked List Cycle
#
#    Given the head of a singly linked list, return the last node in the cycle.
#    If there is no cycle, return None.
#    The "last node" is the node whose next pointer points into the cycle
#    (i.e., it's the tail of the cycle portion).


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_last_node_in_cycle(head):
    pass


# Build: num1 -> num2 -> num3 -> num4 -> (back to num2)
# Cycle: num2 -> num3 -> num4 -> num2
# Last node in cycle: num4
num4 = Node(4)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
num4.next = num2

result = find_last_node_in_cycle(num1)
print(result.value if result else None)

# Build non-cyclic: var1 -> var2 -> var3
var3 = Node(3)
var2 = Node(2, var3)
var1 = Node(1, var2)

print(find_last_node_in_cycle(var1))

# Example Output:
# 4
# None
#
# ------------------------------------------------
