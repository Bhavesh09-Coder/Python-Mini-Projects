# pokemon.py
class Pokemon:
    def __init__(self, name, ptype, health, attack):
        self.name = name
        self.ptype = ptype
        self.health = health
        self.attack = attack

    def __str__(self):
        return f"{self.name} ({self.ptype}) - HP: {self.health}, ATK: {self.attack}"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_fainted(self):
        return self.health == 0
