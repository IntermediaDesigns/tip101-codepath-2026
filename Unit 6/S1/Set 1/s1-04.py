# ------------------------------------------------
#  *                    Problem 4: Find the Middle
#
#    Given the head of a linked list, use the slow-fast pointer technique to
#    find the middle node. If there are two middle nodes, return the second one.
#    After solving, evaluate the time and space complexity of your solution.
#
#    Slow-Fast Pointer: initialize slow and fast pointers at head. Move slow
#    by 1 step and fast by 2 steps each iteration. When fast reaches the end,
#    slow is at the middle.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_element(head):
    pass


# Build: 1 -> 2 -> 3
n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)
print(find_middle_element(n1).value)

# Build: 1 -> 2 -> 3 -> 4
n4b = Node(4)
n3b = Node(3, n4b)
n2b = Node(2, n3b)
n1b = Node(1, n2b)
print(find_middle_element(n1b).value)

# Example Output:
# 2  (middle of 1->2->3)
# 3  (second middle of 1->2->3->4)
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
