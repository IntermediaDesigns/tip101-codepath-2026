# ------------------------------------------------
#  *                    Problem 9: Head and Tail Nodes
#
#    Using the provided Node class, create two nodes:
#    - head with value 100
#    - tail with value 200
#    Then set head to point to tail.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Create and link your nodes here
head = None  # Replace with your code
tail = None  # Replace with your code
# head.next = ???  # Link head to tail

print(head.value)
print(head.next.value)
print(tail.value)
print(tail.next)

# Example Output:
# 100
# 200
# 200
# None
#
# ------------------------------------------------
