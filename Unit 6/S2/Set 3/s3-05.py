# ------------------------------------------------
#  *                    Problem 5: Rotate a Doubly Linked List to the Left
#
#    Given the head of a doubly linked list and a non-negative integer k,
#    rotate the list to the LEFT by k places. Return the new head.
#    After solving, evaluate the time and space complexity of your solution.
#
#    Example: 1 <-> 2 <-> 3 <-> 4 <-> 5, k=2
#    Rotation 1: 2 <-> 3 <-> 4 <-> 5 <-> 1
#    Rotation 2: 3 <-> 4 <-> 5 <-> 1 <-> 2  =>  new head = 3


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


def rotate_doubly_linked_list(head, k):
    pass


def to_string_dll(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " <-> ".join(parts) if parts else "EMPTY"


# Build DLL: 1 <-> 2 <-> 3 <-> 4 <-> 5
vals = [1, 2, 3, 4, 5]
nodes = [Node(v) for v in vals]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
    nodes[i + 1].prev = nodes[i]

print(to_string_dll(nodes[0]))
new_head = rotate_doubly_linked_list(nodes[0], 2)
print(to_string_dll(new_head))

# Build DLL: 0 <-> 1 <-> 2, k=4
vals2 = [0, 1, 2]
nodes2 = [Node(v) for v in vals2]
for i in range(len(nodes2) - 1):
    nodes2[i].next = nodes2[i + 1]
    nodes2[i + 1].prev = nodes2[i]
new_head2 = rotate_doubly_linked_list(nodes2[0], 4)
print(to_string_dll(new_head2))

# Example Output:
# 1 <-> 2 <-> 3 <-> 4 <-> 5
# 3 <-> 4 <-> 5 <-> 1 <-> 2
# 1 <-> 2 <-> 0
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
