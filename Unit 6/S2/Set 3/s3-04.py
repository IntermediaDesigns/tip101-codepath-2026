# ------------------------------------------------
#  *                    Problem 4: Skip and Remove Nodes in a Linked List
#
#    Given the head of a linked list and integers m and n, keep the first m
#    nodes then delete the next n nodes. Repeat this pattern until the end of
#    the list. Return the head of the modified list.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def skip_and_remove(head, m, n):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1->2->3->4->5->6->7->8->9->10, m=2, n=3
nodes = [Node(i) for i in range(1, 11)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

print(to_string(nodes[0]))
print(to_string(skip_and_remove(nodes[0], 2, 3)))

# Build: 1->2->3->4->5->6, m=3, n=1
nodes2 = [Node(i) for i in range(1, 7)]
for i in range(len(nodes2) - 1):
    nodes2[i].next = nodes2[i + 1]
print(to_string(skip_and_remove(nodes2[0], 3, 1)))

# Example Output:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
# 1 -> 2 -> 6 -> 7
# 1 -> 2 -> 3 -> 5 -> 6
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
