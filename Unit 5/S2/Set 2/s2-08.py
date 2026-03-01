# ------------------------------------------------
#  *                    Problem 8: Find Middle Node
#
#    Write a function find_middle_node() that takes in the head of a linked
#    list and returns the middle node. If the list has an even length and two
#    middle nodes, return the first middle node.
#    e.g. "1 -> 2 -> 3 -> 4" returns the node with value 2.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_node(head):
    pass


# Build: num1 -> num2 -> num3 -> num4
num4 = Node(4)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)

mid = find_middle_node(num1)
print(mid.value)

# Example Output:
# 2
#
# ------------------------------------------------
