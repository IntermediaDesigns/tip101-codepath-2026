# ------------------------------------------------
#  *                    Problem 5: Circular Linked List Rotate
#
#    Given the head of a linked list and a non-negative integer k, rotate the
#    list to the RIGHT by k places. Return the head of the rotated list.
#    e.g. rotating [1,2,3,4,5] right by 2 gives [4,5,1,2,3]


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def rotate_right(head, k):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Example 1: 1->2->3->4->5, k=2  =>  4->5->1->2->3
n5 = Node(5); n4 = Node(4, n5); n3 = Node(3, n4); n2 = Node(2, n3); n1 = Node(1, n2)
print(to_string(n1))
print(to_string(rotate_right(n1, 2)))

# Example 2: 1->2->3, k=4  =>  3->1->2
m3 = Node(3); m2 = Node(2, m3); m1 = Node(1, m2)
print(to_string(rotate_right(m1, 4)))

# Example Output:
# 1 -> 2 -> 3 -> 4 -> 5
# 4 -> 5 -> 1 -> 2 -> 3
# 3 -> 1 -> 2
#
# ------------------------------------------------
