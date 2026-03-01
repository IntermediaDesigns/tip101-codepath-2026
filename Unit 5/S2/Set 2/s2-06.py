# ------------------------------------------------
#  *                    Problem 6: Greatest Node
#
#    Write a function find_max() that takes in the head of a linked list where
#    each node has an integer value and returns the maximum value in the list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_max(head):
    pass


# Build: 20 -> 15 -> 30 -> 10
num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)

max_val = find_max(num1)
print(max_val)

# Example Output:
# 30
#
# ------------------------------------------------
