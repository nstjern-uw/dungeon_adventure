import tkinter as tk
from tkinter import messagebox
from adventurer import Adventurer
from dungeon import Dungeon
import random



class DungeonAdventure:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dungeon Adventure")

        self.dungeon = Dungeon(size=5)
        self.adventurer = Adventurer(name="Player")

        self.create_widgets()

    def create_widgets(self):
        # Static stats frame
        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.grid(row=0, column=0, sticky="ns")

        self.stats_label = tk.Label(self.stats_frame, text=str(self.adventurer))
        self.stats_label.pack()

        # Canvas for dungeon map
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.grid(row=0, column=1)

        # Buttons for movement and potions
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.grid(row=1, column=0, columnspan=2)

        # Movement buttons
        tk.Button(self.buttons_frame, text="North", command=lambda: self.move("N")).grid(row=0, column=1)
        tk.Button(self.buttons_frame, text="South", command=lambda: self.move("S")).grid(row=2, column=1)
        tk.Button(self.buttons_frame, text="East", command=lambda: self.move("E")).grid(row=1, column=2)
        tk.Button(self.buttons_frame, text="West", command=lambda: self.move("W")).grid(row=1, column=0)

        # Potion buttons
        tk.Button(self.buttons_frame, text="Use Healing Potion", command=lambda: self.use_potion("healing")).grid(row=3,
                                                                                                                  column=0,
                                                                                                                  columnspan=3,
                                                                                                                  sticky="ew")
        tk.Button(self.buttons_frame, text="Use Vision Potion", command=lambda: self.use_potion("vision")).grid(row=4,
                                                                                                                column=0,
                                                                                                                columnspan=3,
                                                                                                                sticky="ew")

        self.update_map()

    def update_map(self):
        self.canvas.delete("all")
        size = self.dungeon.size
        room_size = 400 // size
        for i in range(size):
            for j in range(size):
                x0, y0 = j * room_size, i * room_size
                x1, y1 = x0 + room_size, y0 + room_size
                room = self.dungeon.grid[i][j]
                color = "white"
                if (i, j) == self.adventurer.position:
                    color = "green"
                elif room.is_entrance:
                    color = "blue"
                elif room.is_exit:
                    color = "red"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
                self.canvas.create_text(
                    x0 + room_size // 2, y0 + room_size // 2, text=str(room)
                )

    def move(self, direction):
        self.adventurer.move(direction, self.dungeon.size)
        x, y = self.adventurer.position
        room = self.dungeon.grid[x][y]

        if room.has_pit:
            damage = random.randint(1, 20)
            self.adventurer.take_damage(damage)
            messagebox.showinfo("Pit!", f"You fell into a pit and lost {damage} HP!")
        if room.has_healing_potion:
            self.adventurer.healing_potions += 1
            room.has_healing_potion = False
            messagebox.showinfo("Potion Found", "You found a healing potion!")
        if room.has_vision_potion:
            self.adventurer.vision_potions += 1
            room.has_vision_potion = False
            messagebox.showinfo("Potion Found", "You found a vision potion!")
        if room.pillar:
            self.adventurer.pillars_found.add(room.pillar)
            room.pillar = None
            messagebox.showinfo("Pillar Found", f"You found the Pillar of {room.pillar}!")

        if self.adventurer.hit_points <= 0:
            self.end_game("lost")
        elif room.is_exit and len(self.adventurer.pillars_found) == 4:
            self.end_game("won")
        else:
            self.update_map()
            self.stats_label.config(text=str(self.adventurer))

    def use_potion(self, potion_type):
        if potion_type == "healing":
            if self.adventurer.healing_potions > 0:
                self.adventurer.use_healing_potion()
                self.stats_label.config(text=str(self.adventurer))
                messagebox.showinfo("Potion Used", "Healing Potion used! HP restored.")
            else:
                messagebox.showwarning("No Potions", "You have no healing potions!")
        elif potion_type == "vision":
            if self.adventurer.vision_potions > 0:
                self.adventurer.vision_potions -= 1
                self.show_vision()
                self.stats_label.config(text=str(self.adventurer))
            else:
                messagebox.showwarning("No Potions", "You have no vision potions!")

    def show_vision(self):
        x, y = self.adventurer.position
        size = self.dungeon.size
        visible_rooms = []

        # Determine rooms within the 3x3 area around the adventurer
        for i in range(max(0, x - 1), min(size, x + 2)):
            for j in range(max(0, y - 1), min(size, y + 2)):
                visible_rooms.append((i, j))

        # Highlight rooms in the canvas
        room_size = 400 // size
        for i, j in visible_rooms:
            x0, y0 = j * room_size, i * room_size
            x1, y1 = x0 + room_size, y0 + room_size
            self.canvas.create_rectangle(x0, y0, x1, y1, outline="gold", width=2)

    def end_game(self, result):
        message = "You won!" if result == "won" else "You lost!"
        tk.messagebox.showinfo("Game Over", message)
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = DungeonAdventure()
    game.run()
