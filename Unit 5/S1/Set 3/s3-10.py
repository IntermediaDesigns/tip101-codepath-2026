# ------------------------------------------------
#  *                    Problem 10: Chase List
#
#    Using the linked list from Problem 9 (cat -> mouse), create a new Node
#    named dog with value "Spike" and point it to cat so the full list is:
#    dog -> cat -> mouse


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


mouse = Node("Jerry")
cat = Node("Tom", mouse)

# Create dog and link it here
dog = None  # Replace with your code

print(dog.value)
print(dog.next is cat)
print(dog.next.value)
print(cat.next is mouse)
print(cat.next.value)
print(mouse.next)

# Example Output:
# Spike
# True
# Tom
# True
# Jerry
# None
#
# ------------------------------------------------
