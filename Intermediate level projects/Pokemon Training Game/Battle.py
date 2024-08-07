# battle.py
from trainer import Trainer

class Battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2

    def start(self):
        print(f"Battle between {self.trainer1.name} and {self.trainer2.name}!")
        while self.trainer1.has_pokemons() and self.trainer2.has_pokemons():
            pokemon1 = self.trainer1.choose_pokemon()
            pokemon2 = self.trainer2.choose_pokemon()

            print(f"{self.trainer1.name} chose {pokemon1.name}")
            print(f"{self.trainer2.name} chose {pokemon2.name}")

            while not pokemon1.is_fainted() and not pokemon2.is_fainted():
                self.attack(pokemon1, pokemon2)
                if pokemon2.is_fainted():
                    print(f"{pokemon2.name} fainted!")
                    break
                self.attack(pokemon2, pokemon1)
                if pokemon1.is_fainted():
                    print(f"{pokemon1.name} fainted!")
                    break

    def attack(self, attacker, defender):
        print(f"{attacker.name} attacks {defender.name}!")
        defender.take_damage(attacker.attack)
        print(f"{defender.name}'s HP: {defender.health}")
