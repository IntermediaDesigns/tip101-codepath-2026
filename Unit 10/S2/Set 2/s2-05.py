# ------------------------------------------------
#  *                    Problem 5: Insert into a Sorted Circular Linked List
#
#    Given a node start_node in a sorted circular linked list, insert insert_val
#    so the list remains sorted. If the list is empty (start_node is None),
#    create a new single-node circular list. Return the original start_node
#    (or the new node if the list was empty).

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert(start_node, insert_val):
    pass


# Helper to print circular linked list (prints up to n nodes to avoid infinite loop)
def print_circular(start, n=10):
    if not start:
        print("Empty")
        return
    result = []
    cur = start
    for _ in range(n):
        result.append(str(cur.val))
        cur = cur.next
        if cur == start:
            break
    print(" -> ".join(result) + " -> (back to start)")


# Example: Circular list 1 -> 3 -> 4 -> (back to 1), insert 2
n1 = Node(3)
n2 = Node(4)
n3 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n1  # circular

result = insert(n1, 2)
print_circular(result)
# Expected Output: 3 -> 4 -> 1 -> 2 -> (back to start)
# (The list 1->2->3->4 is circular; we return the original start node 3)

# Example: Empty list, insert 1
result2 = insert(None, 1)
print_circular(result2)
# Expected Output: 1 -> (back to start)

# ------------------------------------------------
