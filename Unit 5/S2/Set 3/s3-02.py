# ------------------------------------------------
#  *                    Problem 2: Update Linked List Sequence
#
#    Using the provided Node class and the linked list below, update the
#    current list red -> yellow -> blue to be:
#    red -> orange -> yellow -> green -> blue
#    by inserting two new nodes.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


red = Node("red")
yellow = Node("yellow")
blue = Node("blue")
red.next = yellow
yellow.next = blue

print(to_string(red))

# Insert orange and green here to get: red -> orange -> yellow -> green -> blue
orange = None  # Replace with your code
green = None   # Replace with your code
# Update pointers

print(to_string(red))

# Example Output:
# red -> yellow -> blue
# red -> orange -> yellow -> green -> blue
#
# ------------------------------------------------
