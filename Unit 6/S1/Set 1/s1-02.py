# ------------------------------------------------
#  *                    Problem 2: Find Frequency
#
#    Given the head of a linked list and a value val, return the frequency of
#    val in the list.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def count_element(head, val):
    pass


# Build: 3 -> 1 -> 2 -> 1
n4 = Node(1)
n3 = Node(2, n4)
n2 = Node(1, n3)
n1 = Node(3, n2)

print(count_element(n1, 1))
print(count_element(n1, 3))
print(count_element(n1, 5))

# Example Output:
# 2
# 1
# 0
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
