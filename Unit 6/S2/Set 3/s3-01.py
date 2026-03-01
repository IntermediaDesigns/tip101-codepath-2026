# ------------------------------------------------
#  *                    Problem 1: Circular List Length
#
#    A circular linked list is one where the tail node points back at the head.
#    Write a function circular_list_length() that returns the length of a
#    circular linked list.
#    After solving, evaluate the time and space complexity of your solution.
#
#    Circular list diagram:
#    1 -> 2 -> 3
#    ^         |
#    |_________|


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def circular_list_length(head):
    pass


# Build circular list: 1 -> 2 -> 3 -> (back to 1)
n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)
n3.next = n1   # make it circular

print(circular_list_length(n1))

# Build circular list of length 1: node -> itself
solo = Node(42)
solo.next = solo
print(circular_list_length(solo))

# Example Output:
# 3
# 1
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
