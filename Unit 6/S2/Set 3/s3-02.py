# ------------------------------------------------
#  *                    Problem 2: Detect and Remove Cycle in a Linked List
#
#    Given the head of a linked list, remove any cycle present so the list
#    becomes a standard singly linked list. Return the head of the list.
#    After solving, evaluate the time and space complexity of your solution.
#
#    Cycle diagram:
#    1 -> 2 -> 3
#    ^         |
#    |_________|


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def detect_and_remove_cycle(head):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1 -> 2 -> 3 -> (back to 1)
n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)
n3.next = n1   # cycle

result = detect_and_remove_cycle(n1)
print(to_string(result))

# Build: 1 -> 2 -> 3 -> 4 -> (back to 2)
m4 = Node(4)
m3 = Node(3, m4)
m2 = Node(2, m3)
m1 = Node(1, m2)
m4.next = m2   # cycle mid-list

result2 = detect_and_remove_cycle(m1)
print(to_string(result2))

# Example Output:
# 1 -> 2 -> 3
# 1 -> 2 -> 3 -> 4
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
