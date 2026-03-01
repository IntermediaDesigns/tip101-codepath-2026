# ------------------------------------------------
#  *                    Problem 7: Pop Node
#
#    Write a function ll_pop() that takes in the head of a linked list and an
#    index i as parameters. Remove the node at index i and return the head of
#    the list. If i is greater than the list length, do nothing.
#    Hint: Linked lists don't have built-in indices — track them yourself.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def ll_pop(head, i):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: num1 -> num2 -> num3
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)

print(to_string(num1))
head = ll_pop(num1, 1)
print(to_string(head))

# Example Output:
# num1 -> num2 -> num3
# num1 -> num3
#
# ------------------------------------------------
