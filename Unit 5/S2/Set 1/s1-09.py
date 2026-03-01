# ------------------------------------------------
#  *                    Problem 9: Doubly Linked List
#
#    Using the Node class for a doubly linked list below, recreate the list
#    ["Poliwag", "Poliwhirl", "Poliwrath"] as a doubly linked list.
#    Store nodes in variables poliwag, poliwhirl, and poliwrath.
#    Each node should have both next and prev pointers set correctly.


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


# Create your doubly linked list here
poliwag = None      # Replace with your code
poliwhirl = None    # Replace with your code
poliwrath = None    # Replace with your code
# Set next and prev pointers

print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)

# Example Output:
# Poliwag <-> Poliwhirl <-> Poliwrath
#
# ------------------------------------------------
