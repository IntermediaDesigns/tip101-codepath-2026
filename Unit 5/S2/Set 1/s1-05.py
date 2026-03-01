# ------------------------------------------------
#  *                    Problem 5: Replace Node
#
#    Write a function ll_replace() that updates in place every node whose
#    value == original to have value = replacement. The function returns None.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def ll_replace(head, original, replacement):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build: 5 -> 6 -> 5
num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
head = num1

print(to_string(head))
ll_replace(head, 5, "banana")
print(to_string(head))

# Example Output:
# 5 -> 6 -> 5
# banana -> 6 -> banana
#
# ------------------------------------------------
