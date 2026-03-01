# ------------------------------------------------
#  *                    Problem 3: Shuffle Merge
#
#    Given the heads of two singly linked lists, merge their nodes alternately.
#    If one list runs out before the other, append the remaining nodes to the end.
#    Return the head of the merged list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def shuffle_merge(head_a, head_b):
    pass


# Helper to print linked list
def print_list(head):
    result = []
    while head:
        result.append(str(head.value))
        head = head.next
    print(" -> ".join(result))


# Example #1: List 1: 1->2->3, List 2: 4->5->6
a1 = Node(1, Node(2, Node(3)))
b1 = Node(4, Node(5, Node(6)))
print_list(shuffle_merge(a1, b1))
# Expected Output: 1 -> 4 -> 2 -> 5 -> 3 -> 6

# Example #2: List 1: 1->2->3, List 2: 4
a2 = Node(1, Node(2, Node(3)))
b2 = Node(4)
print_list(shuffle_merge(a2, b2))
# Expected Output: 1 -> 4 -> 2 -> 3

# ------------------------------------------------
