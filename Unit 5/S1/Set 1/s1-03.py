# ------------------------------------------------
#  *                    Problem 3: Is Caught
#
#    Using the Pokemon class from Problem 2, update squirtle's is_caught
#    attribute to True. Use print_pokemon() to verify the update.


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


squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()

# Update is_caught here
if squirtle.name == "Squirtle":
    squirtle.is_caught = True

# squirtle.??? = ???

squirtle.print_pokemon()

# Example Output:
# {'name': 'Squirtle', 'types': ['Water'], 'is_caught': False}
# {'name': 'Squirtle', 'types': ['Water'], 'is_caught': True}
#
# ------------------------------------------------
