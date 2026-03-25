# ------------------------------------------------
#  *                    Problem 2: Create Squirtle
#
#    The print_pokemon() method has been added to the Pokemon class below.
#    Step 1: Instantiate an instance of Pokemon and store it in a variable
#            named squirtle with name "Squirtle" and types ["Water"].
#    Step 2: Call the method print_pokemon() on your squirtle instance.


class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })


squirtle = Pokemon("Squirtle", ["Water"])  # Replace with your code
# squirtle.print_pokemon()  # Uncomment after instantiating
print(squirtle.name)  # Should print "Squirtle"
print(squirtle.types)  # Should print ["Water"]
print(squirtle.is_caught)  # Should print False

# Example Output:
# {'name': 'Squirtle', 'types': ['water'], 'is_caught': False}
#
# ------------------------------------------------
