# Mystery Function
# Given the following code, what is the value of output?

def mystery_function(lst1, lst2):
    for num in lst2:
        lst1.append(num)
    return lst1

output = mystery_function([1,2,3,4], [5,6,7,8])

print(output)  # What is the value of output?