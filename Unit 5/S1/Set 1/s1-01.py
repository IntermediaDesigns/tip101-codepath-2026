# ------------------------------------------------
#  *                    Problem 1: Pokemon Class
#
#    Copy the following code into your IDE. Then add a line of code (outside
#    of the class) to instantiate an instance of the Pokemon class and store it
#    in a variable named my_pokemon. The instance should have name "Pikachu"
#    and types ["Electric"].


class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False


# Instantiate my_pokemon here
my_pokemon = Pokemon("Pikachu", ["Electric"])  # Replace with your code

print(my_pokemon.name)  # Should print "Pikachu"
print(my_pokemon.types)  # Should print ["Electric"]

# Example Output: my_pokemon.name should be "Pikachu", my_pokemon.types should be ["Electric"]
#
# ------------------------------------------------
