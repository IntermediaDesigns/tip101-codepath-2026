# ------------------------------------------------
#  *                    Problem 6: List Nodes
#
#    Write a function listify_first_n() that takes in the head of a linked
#    list and a non-negative integer n as parameters. Return a list of the
#    values of the first n nodes. If n is greater than the list length, return
#    all node values.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def listify_first_n(head, n):
    pass


# Build: a -> b -> c
c = Node("c")
b = Node("b", c)
a = Node("a", b)

lst = listify_first_n(a, 2)
print(lst)

# Build: j -> k -> l
l = Node("l")
k = Node("k", l)
j = Node("j", k)

lst2 = listify_first_n(j, 5)
print(lst2)

# Example Output:
# ['a', 'b']
# ['j', 'k', 'l']
#
# ------------------------------------------------
