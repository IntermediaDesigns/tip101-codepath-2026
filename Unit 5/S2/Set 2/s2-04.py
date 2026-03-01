# ------------------------------------------------
#  *                    Problem 4: Linked List Length
#
#    Write a function ll_length() that takes in the head of a linked list and
#    returns the length of the linked list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def ll_length(head):
    pass


# Build: num1 -> num2 -> num3
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)

print(ll_length(num1))

# Empty list
print(ll_length(None))

# Example Output:
# 3
# 0
#
# ------------------------------------------------
