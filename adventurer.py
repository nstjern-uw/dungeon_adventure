import random


class Adventurer:
    def __init__(self, name):
        self.name = name
        self.hit_points = random.randint(75, 100)
        self.healing_potions = 0
        self.vision_potions = 0
        self.pillars_found = set()
        self.position = (0, 0)

    def move(self, direction, dungeon_size):
        x, y = self.position
        if direction == "N" and x > 0:
            self.position = (x - 1, y)
        elif direction == "S" and x < dungeon_size - 1:
            self.position = (x + 1, y)
        elif direction == "E" and y < dungeon_size - 1:
            self.position = (x, y + 1)
        elif direction == "W" and y > 0:
            self.position = (x, y - 1)

    def take_damage(self, amount):
        self.hit_points -= amount

    def use_healing_potion(self):
        if self.healing_potions > 0:
            self.hit_points += random.randint(5, 15)
            self.healing_potions -= 1

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"HP: {self.hit_points}\n"
            f"Healing Potions: {self.healing_potions}\n"
            f"Vision Potions: {self.vision_potions}\n"
            f"Pillars Found: {', '.join(self.pillars_found) or 'None'}"
        )
