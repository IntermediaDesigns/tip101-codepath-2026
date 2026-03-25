# ------------------------------------------------
#  *                    Problem 9: Node Class
#
#    Using the provided Node class below, create two nodes:
#    - node_one with value "a"
#    - node_two with value "b"
#    Do not connect the nodes yet.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Create your nodes here
node_one = Node("a")  # Replace with your code
node_two = Node("b")  # Replace with your code

print(node_one.value)
print(node_one.next)
print(node_two.value)
print(node_two.next)

# Example Output:
# a
# None
# b
# None
#
# ------------------------------------------------
