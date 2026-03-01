# ------------------------------------------------
#  *                    Problem 3: Partition List Around Value
#
#    Given the head of a linked list and a value val, partition the list so
#    that all nodes with values less than val come before nodes with values
#    greater than or equal to val. Return the head of the partitioned list.
#    (Relative order within each partition does not need to be preserved.)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def partition(head, val):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1 -> 4 -> 3 -> 2 -> 5 -> 2, val = 3
n6 = Node(2)
n5 = Node(5, n6)
n4 = Node(2, n5)
n3 = Node(3, n4)
n2 = Node(4, n3)
n1 = Node(1, n2)

print(to_string(n1))
new_head = partition(n1, 3)
print(to_string(new_head))

# Example Output (one valid result):
# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# 1 -> 2 -> 2 -> 4 -> 3 -> 5
# (or any arrangement with all values < 3 before values >= 3)
#
# ------------------------------------------------
