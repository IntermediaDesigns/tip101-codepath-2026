# ------------------------------------------------
#  *                    Problem 5: Restock Inventory
#
#    Write a function restock_inventory() that updates an inventory dictionary
#    based on a restock list. It accepts two parameters:
#      current_inventory: a dictionary mapping items to their current stock
#      restock_list: a dictionary mapping items to the quantity to be added
#    If an item in restock_list is not in current_inventory, it should be added.
#    The function should return the updated current_inventory dictionary.


def restock_inventory(current_inventory, restock_list):
    pass


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}
restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory, restock_list))

# Example Output:
# {'apples': 40, 'bananas': 15, 'oranges': 30, 'pears': 5}
#
# ------------------------------------------------
