# ------------------------------------------------
#  *                    Problem 8: Linked Listify
#
#    Write a function list_to_linked_list() that takes in a Python list lst
#    and converts it to a linked list. Return the head of the linked list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def list_to_linked_list(lst):
    pass


normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)

print(linked_list.value)

current = linked_list
while current:
    end_arrow = " -> " if current.next else "\n"
    print(current.value, end=end_arrow)
    current = current.next

print(linked_list.value)

# Example Output:
# Betty
# Betty -> Veronica -> Archie -> Jughead
# Betty
#
# ------------------------------------------------
