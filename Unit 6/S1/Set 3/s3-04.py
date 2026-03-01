# ------------------------------------------------
#  *                    Problem 4: Does it Cycle?
#
#    Given the head of a linked list, return True if the list has a cycle in
#    it and False otherwise. A cycle exists if a node's next pointer points
#    back to a previous node. Use the fast and slow pointer technique.
#    After solving, evaluate the time and space complexity of your solution.
#
#    Cycle diagram:
#    1 -> 2 -> 3 -> 4
#         ^         |
#         |_________|


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    pass


# Build cyclic list: 1 -> 2 -> 3 -> 4 -> (back to 2)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n4.next = n2

print(has_cycle(n1))

# Build non-cyclic list: 1 -> 2 -> 3
m3 = Node(3)
m2 = Node(2, m3)
m1 = Node(1, m2)
print(has_cycle(m1))

# Example Output:
# True
# False
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
