import random

class adventurer:
    def __init__(self): 
        self.name = ""
        self.hit_points = random.randint(75, 100)
        self.healing_potions = 0
        self.vision_potions = 0
        self.programming_pillars = []
        self.pillar_count = 0

    def set_name(self):
        self.name = input("Enter your name: ")
        print("Your hero's name is " + self.name)

    # def set_hit_points(self):
    #     hitpoints = random.randint(75, 100)
    #     self.hit_points = hitpoints
    #     return self.hit_points
    
    def found_healing_potion(self):
        heal = random.randint(5, 15)
        self.hit_points += heal
        print(f"The healing potion gave you {heal} hitpoints. You now have {self.hit_points} hit points!")


    def pitfall(self):
        damage = random.randint(1, 20)
        self.hit_points -= damage
        print(f"You fell in a pit and lost {damage} hitpoints. You now have {self.hit_points} hit points!")

    def found_programming_pillar(self, pillar):
        if pillar: 
            self.programming_pillars.append(pillar)
            self.pillar_count += 1

    def __str__(self):
        formatted_string = (
            f"Your hero's name is {self.name}!\n"
            f"You have {self.hit_points} hit points. Use them wisely.\n"
            f"You have {self.healing_potions} healing potions.\n"
            f"You have {self.vision_potions} vision potions.\n"
            f"You have found {self.pillar_count} programming pillars. They are {self.programming_pillars}."
        )
        return formatted_string
        

hero = adventurer()
hero.set_name()
print(hero.hit_points)
hero.found_healing_potion()
hero.pitfall()
hero.found_programming_pillar("Inheritance")
print(hero.programming_pillars)
print(str(hero))
    



