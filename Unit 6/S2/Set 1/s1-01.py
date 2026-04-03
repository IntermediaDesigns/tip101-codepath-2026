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
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # A cycle is detected
            # Check if the cycle is circular (points back to head)
            current = slow
            while True:
                if current == head:
                    return True  # It's circular
                current = current.next
                if current == slow:  # Completed one full cycle without finding head
                    break

    return False  # No cycle or not circular


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


# Example Output:
# True
# False
# False
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
#
# ------------------------------------------------
