# ------------------------------------------------
#  *                    Problem 11: Mario Party
#
#    Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list
#    using the Node class below. Store the nodes in variables node_1, node_2,
#    node_3, and node_4.
#    Result: Mario -> Luigi -> Wario -> Toad


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Create your linked list here
node_1 = Node("Mario")  # Replace with your code
node_2 = Node("Luigi")
node_3 = Node("Wario")
node_4 = Node("Toad")

# Link the nodes
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

# Example Output:
# Mario -> Luigi
# Luigi -> Wario
# Wario -> Toad
# Toad -> None
#
# ------------------------------------------------
