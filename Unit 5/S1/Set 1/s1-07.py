# ------------------------------------------------
#  *                    Problem 7: Get Pokemon
#
#    Outside the Pokemon class, write a function get_by_type() that takes in
#    a list of Pokemon instances my_pokemon and a string pokemon_type as
#    parameters. Return a list of all Pokemon that have that type.
#    Hint: Loop over the returned list and print each Pokemon's name to verify.


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

    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)


def get_by_type(my_pokemon, pokemon_type):
    pokemon_of_type = []
    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            pokemon_of_type.append(pokemon.name)
    return pokemon_of_type


jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)

# Example Output:
# [Jigglypuff, Meowth, Pidgeot]  (list of Pokemon objects)
#
# ------------------------------------------------
