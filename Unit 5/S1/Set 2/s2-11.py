# ------------------------------------------------
#  *                    Problem 11: Zodiac Signs
#
#    Create the list ["aries", "taurus", "gemini", "cancer"] as a linked list
#    using the Node class. Store nodes in variables node_1, node_2, node_3,
#    and node_4.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Create your linked list here
node_1 = None  # Replace with your code
node_2 = None
node_3 = None
node_4 = None

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

# Example Output:
# aries -> taurus
# taurus -> gemini
# gemini -> cancer
# cancer -> None
#
# ------------------------------------------------
