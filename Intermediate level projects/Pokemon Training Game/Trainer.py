# trainer.py
from pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if len(self.pokemons) < 6:
            self.pokemons.append(pokemon)
        else:
            print(f"{self.name} already has 6 Pokémon!")

    def choose_pokemon(self):
        print(f"{self.name}'s Pokémon:")
        for i, pokemon in enumerate(self.pokemons):
            print(f"{i + 1}. {pokemon}")
        choice = int(input("Choose a Pokémon by number: ")) - 1
        return self.pokemons[choice]

    def has_pokemons(self):
        return any(pokemon.health > 0 for pokemon in self.pokemons)

    def __str__(self):
        return f"{self.name} - Pokémon: {[pokemon.name for pokemon in self.pokemons]}"
