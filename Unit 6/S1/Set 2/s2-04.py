# ------------------------------------------------
#  *                    Problem 4: Middle Match
#
#    Given the head of a linked list and a value val, use the slow-fast pointer
#    technique to determine if val matches the middle node of the list.
#    If there are two middle nodes, return True if the second middle matches val.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def middle_match(head, val):
    pass


# Build: 1 -> 2 -> 3  (middle = 2)
n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)
print(middle_match(n1, 2))   # True
print(middle_match(n1, 1))   # False

# Build: 1 -> 2 -> 3 -> 4  (second middle = 3)
n4b = Node(4)
n3b = Node(3, n4b)
n2b = Node(2, n3b)
n1b = Node(1, n2b)
print(middle_match(n1b, 3))  # True
print(middle_match(n1b, 2))  # False

# Example Output:
# True
# False
# True
# False
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
