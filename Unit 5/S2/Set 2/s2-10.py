# ------------------------------------------------
#  *                    Problem 10: Double to Single
#
#    Write a function dll_to_sll() that takes in the head of a doubly linked
#    list and recreates it as a singly linked list. Return the head of the
#    new singly linked list.


class SLLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class DLLNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def dll_to_sll(dll_head):
    pass


def to_string(head):
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"


# Build DLL: Ice <-> Water <-> Steam
steam = DLLNode("Steam")
water = DLLNode("Water", steam)
ice = DLLNode("Ice", water)
water.prev = ice
steam.prev = water

sll_head = dll_to_sll(ice)
print(to_string(sll_head))

# Example Output:
# Ice -> Water -> Steam
#
# ------------------------------------------------
