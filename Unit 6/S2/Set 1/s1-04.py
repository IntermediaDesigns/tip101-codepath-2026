# ------------------------------------------------
#  *                    Problem 4: Convert Binary Number in a Linked List to Integer
#
#    Given the head of a linked list where each node value is 0 or 1, return
#    the decimal integer represented by the binary number. The most significant
#    bit is at the head of the list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def binary_to_int(head):
    pass


# Build: 1 -> 0 -> 1  (binary 101 = 5)
num3 = Node(1)
num2 = Node(0, num3)
num1 = Node(1, num2)
print(binary_to_int(num1))

# Build: 1 -> 1 -> 1  (binary 111 = 7)
m3 = Node(1)
m2 = Node(1, m3)
m1 = Node(1, m2)
print(binary_to_int(m1))

# Build: 0  (binary 0 = 0)
z1 = Node(0)
print(binary_to_int(z1))

# Example Output:
# 5
# 7
# 0
#
# ------------------------------------------------
