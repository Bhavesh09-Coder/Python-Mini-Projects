# main.py
from pokemon import Pokemon
from trainer import Trainer
from battle import Battle

def main():
    # Create Pokémon
    pikachu = Pokemon("Pikachu", "Electric", 100, 15)
    bulbasaur = Pokemon("Bulbasaur", "Grass", 120, 12)
    charmander = Pokemon("Charmander", "Fire", 110, 14)
    squirtle = Pokemon("Squirtle", "Water", 130, 10)

    # Create Trainers
    ash = Trainer("Ash")
    misty = Trainer("Misty")

    # Add Pokémon to Trainers
    ash.add_pokemon(pikachu)
    ash.add_pokemon(charmander)
    misty.add_pokemon(squirtle)
    misty.add_pokemon(bulbasaur)

    # Start Battle
    battle = Battle(ash, misty)
    battle.start()

if __name__ == "__main__":
    main()
