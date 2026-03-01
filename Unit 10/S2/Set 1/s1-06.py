# ------------------------------------------------
#  *                    Problem 6: Add Two Numbers Represented By Linked Lists
#
#    Given heads of two linked lists l1 and l2, each representing a non-negative
#    integer stored in reverse order (one digit per node), add the two numbers
#    and return the sum as a linked list in reverse order.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    pass


# Helper to print linked list
def print_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))


# Example: list1: 2->4->3 (represents 342), list2: 5->6->4 (represents 465)
l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(4)))
print_list(add_two_numbers(l1, l2))
# Expected Output: 7 -> 0 -> 8  (represents 807, since 342 + 465 = 807)

# ------------------------------------------------
