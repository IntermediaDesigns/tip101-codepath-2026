# ------------------------------------------------
#  *                    Problem 9: Tom and Jerry
#
#    Using the provided Node class, create a linked list cat -> mouse where:
#    - cat has value "Tom"
#    - mouse has value "Jerry"
#    - cat points to mouse


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Create your nodes here
mouse = None  # Replace with your code
cat = None    # Replace with your code (should point to mouse)

print(cat.value)
print(cat.next.value)
print(mouse.next)

# Example Output:
# Tom
# Jerry
# None
#
# ------------------------------------------------
