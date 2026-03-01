# ------------------------------------------------
#  *                    Problem 1: The Power of One
#
#    The code below creates the linked list Ash -> Misty -> Brock using
#    multiple lines. Refactor it to create the same list in a single line of
#    code using nested constructor calls.
#    Note: The original code also contains a bug — fix it too!


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Original multi-line code (contains a bug — find it!):
# head = Node("Ash")
# misty = Node("Misty")
# brock = Node("Brock")
# head.next = misty
# luigi.next = brock   # <-- bug here

# Recreate Ash -> Misty -> Brock in a SINGLE LINE below:
head = None  # Replace with your single-line nested constructor call


# Verify:
print(head.value, "->", head.next.value, "->", head.next.next.value)
print(head.next.next.next)

# Example Output:
# Ash -> Misty -> Brock
# None
#
# ------------------------------------------------
