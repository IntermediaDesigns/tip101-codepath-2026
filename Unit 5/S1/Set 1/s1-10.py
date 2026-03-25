# ------------------------------------------------
#  *                    Problem 10: Linking Nodes
#
#    Building off Problem 9, link the two nodes together by setting node_one's
#    next attribute to point to node_two.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


node_one = Node("a")
node_two = Node("b")

# Link the nodes here
node_one.next = node_two


print(node_one.value)
print(node_one.next.value)
print(node_two.value)

# Example Output:
# a
# b
# b
#
# ------------------------------------------------
