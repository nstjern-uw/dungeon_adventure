import random


class Room:
    def __init__(self):
        self.has_healing_potion = random.random() < 0.1
        self.has_vision_potion = random.random() < 0.1
        self.has_pit = random.random() < 0.1
        self.is_entrance = False
        self.is_exit = False
        self.pillar = None  # Can be one of "A", "E", "I", "P" for the Pillars

    def set_entrance(self):
        self.is_entrance = True

    def set_exit(self):
        self.is_exit = True

    def set_pillar(self, pillar):
        self.pillar = pillar

    def clear_items(self):
        self.has_healing_potion = False
        self.has_vision_potion = False
        self.has_pit = False

    def __str__(self):
        if self.is_entrance:
            return "i"
        if self.is_exit:
            return "O"
        if self.pillar:
            return self.pillar
        if self.has_pit:
            return "X"
        if self.has_healing_potion and self.has_vision_potion:
            return "M"
        if self.has_healing_potion:
            return "H"
        if self.has_vision_potion:
            return "V"
        return " "
