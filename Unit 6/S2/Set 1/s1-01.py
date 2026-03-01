# ------------------------------------------------
#  *                    Problem 1: Detect Circular Linked List
#
#    A circular linked list is one where the tail node points back at the head
#    node (not just any cycle). Write a function is_circular() that returns
#    True if the linked list is circular and False otherwise.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_circular(head):
    pass


# Build circular list: num1 -> num2 -> num3 -> num1
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
num3.next = num1   # tail points to head -> circular

print(is_circular(num1))

# Build non-circular list: var1 -> var2 -> var3
var3 = Node(3)
var2 = Node(2, var3)
var1 = Node(1, var2)

print(is_circular(var1))

# Build cycle that is NOT circular: 1 -> 2 -> 3 -> (back to 2, not head)
c3 = Node(3)
c2 = Node(2, c3)
c1 = Node(1, c2)
c3.next = c2   # cycle but not circular

print(is_circular(c1))

# Example Output:
# True
# False
# False
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
