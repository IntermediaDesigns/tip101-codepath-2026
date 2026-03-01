# ------------------------------------------------
#  *                    Problem 2: Find Max
#
#    Given the head of a linked list where each node is an integer value,
#    return the maximum value in the linked list.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_max(head):
    pass


# Build: 5 -> 6 -> 7 -> 8
n4 = Node(8)
n3 = Node(7, n4)
n2 = Node(6, n3)
n1 = Node(5, n2)
print(find_max(n1))

# Build: 3 -> 1 -> 9 -> 2
m4 = Node(2)
m3 = Node(9, m4)
m2 = Node(1, m3)
m1 = Node(3, m2)
print(find_max(m1))

# Example Output:
# 8
# 9
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
