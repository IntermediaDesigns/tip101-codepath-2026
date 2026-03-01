# ------------------------------------------------
#  *                    Problem 4: Get Tail
#
#    Write a function get_tail() that takes in the head of a linked list as a
#    parameter and returns the value of the tail node. If the list is empty,
#    return None.
#    Note: The "tail" is the last element, like lst[-1] of a normal list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def get_tail(head):
    pass


# Build: num1 -> num2 -> num3
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)

head = num1
tail = get_tail(head)
print(tail)

# Example Output:
# num3
#
# ------------------------------------------------
