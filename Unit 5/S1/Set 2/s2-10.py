# ------------------------------------------------
#  *                    Problem 10: Middle Node
#
#    Using the linked list from Problem 9 (head -> tail), create a new Node
#    named middle with value 150 and insert it between head and tail.
#    Result: head -> middle -> tail


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


head = Node(100)
tail = Node(200)
head.next = tail

# Create and insert the middle node here
middle = None  # Replace with your code
# Update pointers so: head -> middle -> tail

print(head.next.value)
print(middle.next.value)
print(tail.next)

# Example Output:
# 150
# 200
# None
#
# ------------------------------------------------
