# ------------------------------------------------
#  *                    Problem 3: Delete N Nodes after M Nodes
#
#    Given the head of a linked list and integers m and n, traverse the list
#    and repeatedly: keep the first m nodes, then remove the next n nodes.
#    Continue until the end of the list. Return the head of the modified list.

class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

def delete_nodes(head, m, n):
    pass


# Helper to print linked list
def print_list(head):
    result = []
    while head:
        result.append(str(head.value))
        head = head.next
    print(" -> ".join(result))


# Example #1: 1->2->3->4->5->6->7->8->9->10->11->12->13, m=2, n=3
head1 = Node(1)
cur = head1
for v in range(2, 14):
    cur.next = Node(v)
    cur = cur.next

print_list(delete_nodes(head1, 2, 3))
# Expected Output: 1 -> 2 -> 6 -> 7 -> 11 -> 12

# Example #2: 1->2->3->4->5->6->7->8->9->10->11, m=1, n=3
head2 = Node(1)
cur = head2
for v in range(2, 12):
    cur.next = Node(v)
    cur = cur.next

print_list(delete_nodes(head2, 1, 3))
# Expected Output: 1 -> 5 -> 9

# ------------------------------------------------
