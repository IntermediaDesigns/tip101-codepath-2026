# ------------------------------------------------
#  *                    Problem 11: Update Chase
#
#    Using the linked list from Problem 10 (dog -> cat -> mouse), remove the
#    dog node and add a new node cheese with value "Gouda" to the end so the
#    resulting list is: cat -> mouse -> cheese


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


mouse = Node("Jerry")
cat = Node("Tom", mouse)
dog = Node("Spike", cat)

# Remove dog from the chain and add cheese to the end
cheese = None  # Replace with your code
# Update pointers here

# Verify: cat -> mouse -> cheese
print(cat.value)
print(cat.next.value)
print(mouse.next.value)
print(cheese.next)

# Example Output:
# Tom
# Jerry
# Gouda
# None
#
# ------------------------------------------------
