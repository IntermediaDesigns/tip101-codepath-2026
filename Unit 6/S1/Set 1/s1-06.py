# ------------------------------------------------
#  *                    Problem 6: Put it in Reverse
#
#    Given the head of a singly linked list, reverse the list in place and
#    return the head of the reversed list.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to the next node

    return prev  # 'prev' is the new head of the reversed list


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1 -> 2 -> 3 -> 4
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(to_string(n1))
new_head = reverse(n1)
print(to_string(new_head))

# Example Output:
# 1 -> 2 -> 3 -> 4
# 4 -> 3 -> 2 -> 1
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
