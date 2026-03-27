# ------------------------------------------------
#  *                    Problem 2: Convert to Linked List
#
#    Using the provided Node class, create the Python list
#    ["Jigglypuff", "Wigglytuff"] as a linked list.
#    Store nodes in variables node_1 and node_2.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Create your linked list here
node_1 = Node("Jigglypuff", node_2)  # Replace with your code
node_2 = Node("Wigglytuff")  # Replace with your code

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

# Example Output:
# Jigglypuff -> Wigglytuff
# Wigglytuff -> None
#
# ------------------------------------------------
