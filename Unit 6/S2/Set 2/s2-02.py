# ------------------------------------------------
#  *                    Problem 2: Collect Nodes of a Cycle in a Linked List
#
#    Given the head of a linked list, return the values of any cycle in the
#    linked list as a Python list. If there is no cycle, return an empty list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def collect_cycle_nodes(head):
    pass


# Build: num1 -> num2 -> num3 -> num4 -> (back to num2)
# Cycle: num2 -> num3 -> num4 -> num2
num4 = Node(4)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
num4.next = num2

lst = collect_cycle_nodes(num1)
print(lst)

# Build: var1 -> var2 -> var3 -> var4 (no cycle)
var4 = Node(4)
var3 = Node(3, var4)
var2 = Node(2, var3)
var1 = Node(1, var2)

lst2 = collect_cycle_nodes(var1)
print(lst2)

# Example Output:
# [2, 3, 4]
# []
#
# ------------------------------------------------
