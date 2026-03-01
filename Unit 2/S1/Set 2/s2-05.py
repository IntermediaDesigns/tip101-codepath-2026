# ------------------------------------------------
#  *                    Problem 5: Merge Catalogs
#
#    Write a function merge_catalogs() that combines two product catalogs, catalog1
#    and catalog2 as parameters. Each is a dictionary mapping product names to prices.
#    If the same product exists in both catalogs, the price from catalog2 should
#    overwrite the price in catalog1. Return the updated catalog1 dictionary.


def merge_catalogs(catalog1, catalog2):
    pass


catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))

# Example Output: {'apple': 1.0, 'banana': 0.75, 'cherry': 1.25}
#
# ------------------------------------------------
