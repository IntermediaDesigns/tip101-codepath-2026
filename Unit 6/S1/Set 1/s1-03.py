# ------------------------------------------------
#  *                    Problem 3: Remove Tail
#
#    The code below attempts to remove the tail of a singly linked list but
#    has a bug! Create your own test cases, use print statements and the stack
#    trace to identify and fix the bug so the function correctly removes the
#    tail of the list.


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug!
def remove_tail(head):
    if head is None:          # If the list is empty, return None
        return None
    if head.next is None:     # If there's only one node, removing it leaves the list empty
        return None
    # Start from the head and find the second-to-last node
    current = head
    while current.next.next:
        current = current.next
    current.next = None       # Remove the last node by setting second-to-last node to None
    return head


# Test cases — add your own to find and fix the bug!
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print("Before:")
print_list(n1)
result = remove_tail(n1)  # Attempt to remove tail (4)
print("After:")
print_list(result)

# Expected Output:
# Before: 1 -> 2 -> 3 -> 4
# After:  1 -> 2 -> 3
#
# ------------------------------------------------
