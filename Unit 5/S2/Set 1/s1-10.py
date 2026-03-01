# ------------------------------------------------
#  *                    Problem 10: Print Backwards
#
#    Write a function print_reverse() that takes in the tail of a doubly linked
#    list and prints the values in reverse order, each separated by a space.


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def print_reverse(tail):
    pass


# Build doubly linked list: Poliwag <-> Poliwhirl <-> Poliwrath
poliwag = Node("Poliwag")
poliwhirl = Node("Poliwhirl")
poliwrath = Node("Poliwrath")

poliwag.next = poliwhirl
poliwhirl.prev = poliwag
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl

# (head) poliwag     (tail) poliwrath
print_reverse(poliwrath)

# Example Output:
# Poliwrath Poliwhirl Poliwag
#
# ------------------------------------------------
