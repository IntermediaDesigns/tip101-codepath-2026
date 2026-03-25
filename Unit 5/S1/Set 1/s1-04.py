# ------------------------------------------------
#  *                    Problem 4: Catch Pokemon
#
#    Update the Pokemon class with a new method catch() that takes no
#    parameters except self. The method should update the Pokemon's is_caught
#    attribute to True and not return any value.


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

    def catch(self):
        self.is_caught = True
        


my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()
my_pokemon.catch()
my_pokemon.print_pokemon()

# Example Output:
# {'name': 'rattata', 'types': ['Normal'], 'is_caught': False}
# {'name': 'rattata', 'types': ['Normal'], 'is_caught': True}
#
# ------------------------------------------------
