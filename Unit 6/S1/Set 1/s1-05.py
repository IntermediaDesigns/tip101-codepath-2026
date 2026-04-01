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
    # Step 1: Find the middle of the linked list using slow-fast pointer technique
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    prev = None
    current = slow

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Step 3: Compare the first half and the reversed second half
    left = head
    right = prev  # 'prev' is now the head of the reversed second half

    while right:  # Only need to compare until 'right' is exhausted
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True


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
