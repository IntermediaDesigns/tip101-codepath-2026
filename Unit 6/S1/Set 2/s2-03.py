# ------------------------------------------------
#  *                    Problem 3: Remove First Value
#
#    The code below attempts to remove the first node with a given value from
#    a singly linked list but has a bug! Create your own test cases, use print
#    statements and the stack trace to find and fix the bug.


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


# Function with a bug!
def remove_by_value(head, val):
    if head is None:
        return head
    if head.value == val:
        return head.next
    current = head.next
    previous = head
    while current.next:           # Bug is here — check the loop condition
        if current.value == val:
            previous.next = current.next
            return head
        previous = current
        current = current.next
    return head


# Test cases — add your own to find and fix the bug!
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print("Before:")
print_list(n1)
result = remove_by_value(n1, 3)
print("After (remove 3):")
print_list(result)

# Also test removing the last element:
n4b = Node(4)
n3b = Node(3, n4b)
n2b = Node(2, n3b)
n1b = Node(1, n2b)
result2 = remove_by_value(n1b, 4)
print("After (remove 4 / tail):")
print_list(result2)

# Expected Output:
# Before:            1 -> 2 -> 3 -> 4
# After (remove 3):  1 -> 2 -> 4
# After (remove 4):  1 -> 2 -> 3
#
# ------------------------------------------------
