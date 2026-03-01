# ------------------------------------------------
#  *                    Problem 2: Reverse Linked List
#
#    Given the head of a singly linked list, reverse the list and return
#    the head of the reversed list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):
    pass


# Helper to print linked list
def print_list(head):
    result = []
    while head:
        result.append(str(head.value))
        head = head.next
    print(" -> ".join(result))


# Example: 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node(4))))
print_list(reverse(head))
# Expected Output: 4 -> 3 -> 2 -> 1

# ------------------------------------------------
