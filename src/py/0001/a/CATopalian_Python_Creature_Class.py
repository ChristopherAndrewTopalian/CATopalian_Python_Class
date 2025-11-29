# CATopalian_Python_Creature_Class.py

# base creature data
creatureData = [
    {
        "name": "Sparkling",
        "power": "Lightning Burst",
        "hp": 35,
        "type": "Electric"
    },
    {
        "name": "Flarecub",
        "power": "Ember Roar",
        "hp": 39,
        "type": "Fire"
    }
]

####

# fibn.py
# find item by name (case insensitive)
def fibn(array, name):
    for item in array:
        if item["name"].lower() == name.lower():
            return item
    return None

####

class Creature:
    def __init__(self, info):
        # info is a dictionary with name, power, hp, etc.
        self.name = info["name"]
        self.power = info["power"]
        self.hp = info["hp"]
        self.type = info["type"]

    def sayName(self):
        print(self.name)

    def attack(self):
        print(self.name + " used " + self.power)

####

class Sparkling(Creature):
    def __init__(self, info):
        super().__init__(info)

    def specialMove(self):
        print(self.name + " unleashed Thunder Spiral!")

####

sparkling = Sparkling(fibn(creatureData, "Sparkling"))

####

sparkling.specialMove()

####

"""
Sparkling unleashed Thunder Spiral!
"""

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

