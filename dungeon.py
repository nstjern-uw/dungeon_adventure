import random
from room import Room


class Dungeon:
    def __init__(self, size=5):
        self.size = size
        self.grid = [[Room() for _ in range(size)] for _ in range(size)]
        self.place_special_rooms()

    def place_special_rooms(self):
        entrance = (0, 0)
        exit_ = (self.size - 1, self.size - 1)
        self.grid[entrance[0]][entrance[1]].set_entrance()
        self.grid[exit_[0]][exit_[1]].set_exit()

        pillars = ["A", "E", "I", "P"]
        random.shuffle(pillars)
        for pillar in pillars:
            while True:
                x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
                if not self.grid[x][y].is_entrance and not self.grid[x][y].is_exit and not self.grid[x][y].pillar:
                    self.grid[x][y].set_pillar(pillar)
                    break

    def __str__(self):
        return "\n".join(
            " ".join(str(self.grid[i][j]) for j in range(self.size))
            for i in range(self.size)
        )

