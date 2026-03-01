# ------------------------------------------------
#  *                    Problem 2: Frequency Map
#
#    Given the head of a linked list, return a dictionary that maps each
#    unique element in the list to its frequency.
#    After solving, evaluate the time and space complexity of your solution.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def frequency_map(head):
    pass


# Build: 1 -> 2 -> 3 -> 4 -> 2 -> 3
n6 = Node(3)
n5 = Node(2, n6)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(frequency_map(n1))

# Build: 5 -> 5 -> 5
m3 = Node(5)
m2 = Node(5, m3)
m1 = Node(5, m2)
print(frequency_map(m1))

# Example Output:
# {1: 1, 2: 2, 3: 2, 4: 1}
# {5: 3}
#
# Time Complexity:  O(?)
# Space Complexity: O(?)
#
# ------------------------------------------------
