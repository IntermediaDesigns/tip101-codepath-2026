# ------------------------------------------------
#  *                    Problem 6: Merge Nodes Between Zeros in a Linked List
#
#    Given the head of a linked list with integers separated by 0s, merge the
#    nodes between each pair of 0s into a single node whose value is the sum
#    of all the merged nodes. Remove all zeroes from the result. The head and
#    tail of the input are always 0s. Return the head of the merged list.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_nodes(head):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0
# Expected: 4 -> 11  (3+1=4, 4+5+2=11)
vals1 = [0, 3, 1, 0, 4, 5, 2, 0]
nodes1 = [Node(v) for v in vals1]
for i in range(len(nodes1) - 1):
    nodes1[i].next = nodes1[i + 1]

print(to_string(nodes1[0]))
print(to_string(merge_nodes(nodes1[0])))

# Build: 0 -> 1 -> 0 -> 3 -> 0 -> 2 -> 2 -> 0
# Expected: 1 -> 3 -> 4  (1, 3, 2+2=4)
vals2 = [0, 1, 0, 3, 0, 2, 2, 0]
nodes2 = [Node(v) for v in vals2]
for i in range(len(nodes2) - 1):
    nodes2[i].next = nodes2[i + 1]

print(to_string(merge_nodes(nodes2[0])))

# Example Output:
# 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0
# 4 -> 11
# 1 -> 3 -> 4
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
