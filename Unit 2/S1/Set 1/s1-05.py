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
    #Loop through restock_list
    for item in restock_list:
    #Check if item is not in current_inventory, it should be added.
        if item not in current_inventory:
            current_inventory[item] = restock_list[item]
    #Check if the item is in current_inventory, add quantity to the current_inventory
        else:
            current_inventory[item] += restock_list[item]
    #Return the updated current_inventory dictionary
    return current_inventory

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
