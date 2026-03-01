# ------------------------------------------------
#  *                    Problem 5: Are We There Yet?
#
#    Given the head of a linked list, return the length of its cycle.
#    A cycle exists if a node's next pointer points back to a previous node.
#    Use the fast and slow pointer technique.
#    After solving, evaluate the time and space complexity of your solution.
#
#    Cycle diagram:
#    1 -> 2 -> 3 -> 4
#         ^         |
#         |_________|  (cycle length = 3: nodes 2, 3, 4)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def cycle_length(head):
    pass


# Build cyclic list: 1 -> 2 -> 3 -> 4 -> (back to 2)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n4.next = n2

print(cycle_length(n1))

# Build non-cyclic list: 1 -> 2 -> 3
m3 = Node(3)
m2 = Node(2, m3)
m1 = Node(1, m2)
print(cycle_length(m1))

# Example Output:
# 3
# 0
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
