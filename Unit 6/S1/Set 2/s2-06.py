# ------------------------------------------------
#  *                    Problem 6: Was That a Crit?
#
#    Given the head of a singly linked list, return the number of critical
#    points. A critical point is a local minima or maxima.
#    - Head and tail nodes are NOT critical points.
#    - Local minima: both neighbors are greater than the current node.
#    - Local maxima: both neighbors are less than the current node.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def count_critical_points(head):
    pass


# Build: 1 -> 2 -> 3 -> 3 -> 3 -> 5 -> 1 -> 3
n8 = Node(3)
n7 = Node(1, n8)
n6 = Node(5, n7)
n5 = Node(3, n6)
n4 = Node(3, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(count_critical_points(n1))

# Build: 1 -> 3 -> 2 -> 4 -> 1
m5 = Node(1)
m4 = Node(4, m5)
m3 = Node(2, m4)
m2 = Node(3, m3)
m1 = Node(1, m2)
print(count_critical_points(m1))

# Example Output:
# 2  (local max: 5, local min: 1)
# 2  (local max: 3, local min: 2)
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
