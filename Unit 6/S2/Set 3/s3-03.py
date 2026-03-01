# ------------------------------------------------
#  *                    Problem 3: Merge Two Sorted Linked Lists
#
#    Given the heads of two sorted linked lists, merge them into one sorted
#    linked list by splicing together the nodes of the input lists. Return
#    the head of the merged list.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_two_lists(head_a, head_b):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# List 1: 1 -> 2 -> 4,  List 2: 2 -> 3 -> 4
a3 = Node(4); a2 = Node(2, a3); a1 = Node(1, a2)
b3 = Node(4); b2 = Node(3, b3); b1 = Node(2, b2)
print(to_string(merge_two_lists(a1, b1)))

# List 1: 1 -> 3 -> 5,  List 2: 2 -> 4 -> 6
c3 = Node(5); c2 = Node(3, c3); c1 = Node(1, c2)
d3 = Node(6); d2 = Node(4, d3); d1 = Node(2, d2)
print(to_string(merge_two_lists(c1, d1)))

# List 1: empty,  List 2: 1
print(to_string(merge_two_lists(None, Node(1))))

# Example Output:
# 1 -> 2 -> 2 -> 3 -> 4 -> 4
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 1
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
