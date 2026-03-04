# ------------------------------------------------
#  *                    Problem 2: Create a Dictionary
#
#    Write a function create_dictionary() that takes in a list of keys and a list
#    of values as parameters. The function returns a dictionary where each item in
#    keys is paired with a corresponding item in values.
#    keys[i] should be paired with values[i] where 0 <= i <= len(keys).
#    You may assume keys and values are the same length.


def create_dictionary(keys, values):
    #Create empty dictionary
    myDict = {}
    #Loop though each element
    for i in range(len(keys)):

    #Add the key and value to dictionary
        myDict[keys[i]] = values[i]

    #Return the dictionary
    return myDict


keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))

# Example Output:
# {'peanut': 'butter', 'dragon': 'fly', 'star': 'fish', 'pop': 'corn', 'space': 'ship'}
#
# ------------------------------------------------
