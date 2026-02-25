# Find Product

def find_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

print(find_product([1, 2, 3, 4]))  # Should print 24
print(find_product([0, 2, 3, 4]))  # Should print 0