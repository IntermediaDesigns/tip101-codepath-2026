# ------------------------------------------------
#  *                    Problem 5: Delete Tail
#
#    Write a function delete_tail() that takes in the head of a linked list
#    and removes the tail node from the end of the list in place.
#    The function does not need to return any value.
#    Note: The "tail" is the last element, like lst[-1] of a normal list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delete_tail(head):
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
delete_tail(num1)
print(to_string(num1))

# Example Output:
# num1 -> num2 -> num3
# num1 -> num2
#
# ------------------------------------------------
