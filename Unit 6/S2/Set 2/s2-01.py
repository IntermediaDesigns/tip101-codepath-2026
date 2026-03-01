# ------------------------------------------------
#  *                    Problem 1: Convert a Singly Linked List to a Circular Linked List
#
#    Write a function make_circular() that transforms a singly linked list into
#    a circular linked list by making the tail point back to the head. Return
#    the head of the linked list.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def make_circular(head):
    pass


# Build: num1 -> num2 -> num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

head = make_circular(num1)

# Verify: traverse 6 steps to confirm the cycle
current = head
for _ in range(6):
    print(current.value, end=" -> ")
print("...")

# Example Output:
# 1 -> 2 -> 3 -> 1 -> 2 -> 3 -> ...
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
