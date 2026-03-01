# ------------------------------------------------
#  *                    Problem 6: Reverse Them, K?
#
#    Given the head of a singly linked list and an integer k, reverse the
#    first k elements of the linked list and return the new head.
#    If k is larger than the length of the list, reverse the entire list.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_first_k(head, k):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 1 -> 2 -> 3 -> 4 -> 5, k = 3
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(to_string(n1))
new_head = reverse_first_k(n1, 3)
print(to_string(new_head))

# Build: 1 -> 2 -> 3, k = 10 (k > length, reverse all)
m3 = Node(3)
m2 = Node(2, m3)
m1 = Node(1, m2)
print(to_string(reverse_first_k(m1, 10)))

# Example Output:
# 1 -> 2 -> 3 -> 4 -> 5
# 3 -> 2 -> 1 -> 4 -> 5
# 3 -> 2 -> 1
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
