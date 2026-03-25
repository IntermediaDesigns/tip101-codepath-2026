# ------------------------------------------------
#  *                    Problem 8: Pokemon Evolution
#
#    Each Pokemon instance now has an evolution attribute that is either None
#    or another Pokemon instance. Write a function get_evolutionary_line() that
#    takes in a Pokemon object starter_pokemon and returns a list of itself and
#    all Pokemon it can evolve into.


class Pokemon:
    def __init__(self, name, types, evolution=None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })


def get_evolutionary_line(starter_pokemon):
    evolutionary_line = []
    current_pokemon = starter_pokemon
    while current_pokemon is not None:
        evolutionary_line.append(current_pokemon.name)
        current_pokemon = current_pokemon.evolution
    return evolutionary_line


charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)

# Example Output:
# ['Charmander', 'Charmeleon', 'Charizard']
# ['Charmeleon', 'Charizard']
# ['Charizard']
#
# ------------------------------------------------
