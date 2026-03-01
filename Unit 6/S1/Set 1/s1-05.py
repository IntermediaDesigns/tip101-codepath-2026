# ------------------------------------------------
#  *                    Problem 5: Is Palindrome?
#
#    Given the head of a singly linked list, return True if the values form a
#    palindrome, False otherwise. Use the two-pointer technique in your solution.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindrome(head):
    pass


# Build: 1 -> 2 -> 1
n3 = Node(1)
n2 = Node(2, n3)
n1 = Node(1, n2)
print(is_palindrome(n1))

# Build: 1 -> 2 -> 3
n3b = Node(3)
n2b = Node(2, n3b)
n1b = Node(1, n2b)
print(is_palindrome(n1b))

# Build: 1 -> 2 -> 2 -> 1
n4c = Node(1)
n3c = Node(2, n4c)
n2c = Node(2, n3c)
n1c = Node(1, n2c)
print(is_palindrome(n1c))

# Example Output:
# True
# False
# True
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
