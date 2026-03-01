# ------------------------------------------------
#  *                    Problem 5: Where Do We Begin?
#
#    A linked list has a cycle if the tail points back to a previous node.
#    Given the head of a linked list, use the fast and slow pointer method to
#    find and return the node where the cycle starts. If no cycle, return None.
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


def get_loop_start(head):
    pass


# Build cyclic list: 1 -> 2 -> 3 -> 4 -> (back to 2)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n4.next = n2   # cycle: 4 points back to 2

result = get_loop_start(n1)
print(result.value if result else None)

# Build non-cyclic list: 1 -> 2 -> 3
m3 = Node(3)
m2 = Node(2, m3)
m1 = Node(1, m2)
print(get_loop_start(m1))

# Example Output:
# 2
# None
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
