# ------------------------------------------------
#  *                    Problem 4: Increment Linked List Node Values
#
#    Write a function increment_ll() that takes in the head of a linked list
#    of integer values and increments each node's value by 1. Return the head
#    of the modified list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def increment_ll(head):
    pass


# Build: 5 -> 6 -> 7
n3 = Node(7)
n2 = Node(6, n3)
n1 = Node(5, n2)
my_list = n1

print(my_list.value)
my_list = increment_ll(my_list)
print(my_list.value)
my_list = increment_ll(my_list)
print(my_list.value)

# Example Output:
# 5
# 6
# 7
#
# ------------------------------------------------
