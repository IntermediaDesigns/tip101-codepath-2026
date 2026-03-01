# ------------------------------------------------
#  *                    Problem 12: Chase String
#
#    Write a function chase_list() that takes in the head of a linked list and
#    returns a string linking together all values with the separator "chases".
#    Note: The "head" is the first node, like lst[0] of a normal list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def chase_list(head):
    pass


dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))

# Example Output:
# Spike chases Tom chases Jerry chases Gouda
#
# ------------------------------------------------
