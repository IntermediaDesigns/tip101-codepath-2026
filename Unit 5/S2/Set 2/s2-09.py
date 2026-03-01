# ------------------------------------------------
#  *                    Problem 9: Create Double Links
#
#    Update the Node constructor below to support a prev attribute so that
#    the code creates a doubly linked list with head <-> tail.
#    Then set the correct next and prev pointers between head and tail.


class Node:
    def __init__(self, value, next=None):  # Add prev parameter here
        self.value = value
        self.next = next
        # Add self.prev here


head = Node("First")
tail = Node("Last")
head.next = tail
# tail.prev = head  # Uncomment after updating the constructor

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)

# Example Output:
# First <-> Last
# First <-> Last
#
# ------------------------------------------------
