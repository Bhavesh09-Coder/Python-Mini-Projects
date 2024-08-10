## Real-Time Strategy Game :
import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.resources = 100
        self.buildings = []
        self.units = []
        self.unit_count = 0

    def gather_resources(self):
        gathered = random.randint(10, 20)
        self.resources += gathered
        print(f"{self.name} gathered {gathered} resources. Total resources: {self.resources}")

    def build_structure(self, structure_type):
        if self.resources >= 50:
            self.resources -= 50
            self.buildings.append(structure_type)
            print(f"{self.name} built a {structure_type}. Remaining resources: {self.resources}")
        else:
            print(f"{self.name} does not have enough resources to build a {structure_type}.")

    def train_unit(self):
        if self.resources >= 30:
            self.resources -= 30
            self.unit_count += 1
            unit = Unit(f"Unit_{self.unit_count}", self)
            self.units.append(unit)
            print(f"{self.name} trained {unit.name}. Remaining resources: {self.resources}")
        else:
            print(f"{self.name} does not have enough resources to train a unit.")

class Unit:
    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.health = 100
        self.attack_power = 10

    def attack(self, target_unit):
        damage = random.randint(5, self.attack_power)
        target_unit.health -= damage
        print(f"{self.name} attacked {target_unit.name} for {damage} damage. {target_unit.name} health: {target_unit.health}")
        if target_unit.health <= 0:
            print(f"{target_unit.name} has been defeated!")

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    players = [player1, player2]
    current_player = 0

    while True:
        player = players[current_player]
        print(f"\n{player.name}'s turn:")
        print("1. Gather resources")
        print("2. Build structure")
        print("3. Train unit")
        print("4. Attack")
        print("5. End turn")

        choice = input("Choose an action: ")

        if choice == '1':
            player.gather_resources()
        elif choice == '2':
            structure = input("Enter structure type (e.g., Barracks): ")
            player.build_structure(structure)
        elif choice == '3':
            player.train_unit()
        elif choice == '4':
            if player.units and any(unit.health > 0 for unit in player.units):
                enemy = players[(current_player + 1) % 2]
                if enemy.units and any(unit.health > 0 for unit in enemy.units):
                    attacker = player.units[0]
                    target = enemy.units[0]
                    attacker.attack(target)
                else:
                    print(f"{enemy.name} has no units to attack.")
            else:
                print(f"{player.name} has no units to attack with.")
        elif choice == '5':
            current_player = (current_player + 1) % 2
        else:
            print("Invalid choice. Try again.")

        time.sleep(1)

if __name__ == "__main__":
    main()
