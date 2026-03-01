# ------------------------------------------------
#  *                    Problem 9: Convert Singly Linked List to Doubly Linked List
#
#    The singly linked list below has next pointers set. Update the code to
#    also set the prev pointers so it becomes a doubly linked list:
#    Crazy in Love <-> Formation <-> Texas Hold 'Em


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold 'Em")

crazy_in_love.next = formation
formation.next = texas_hold_em

# Set prev pointers here to make it a doubly linked list
# formation.prev = ???
# texas_hold_em.prev = ???

print(crazy_in_love.value, "<->", formation.value, "<->", texas_hold_em.value)
print(texas_hold_em.prev.value, "<->", formation.prev.value)

# Example Output:
# Crazy in Love <-> Formation <-> Texas Hold 'Em
# Formation <-> Crazy in Love
#
# ------------------------------------------------
