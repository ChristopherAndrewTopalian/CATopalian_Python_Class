# CATopalian_Python_Pokemon_Class.py

# pokemon data list
pokemon_data = [
    {
        'name': 'Pikachu',
        'power': 'Thunderbolt',
        'hp': 35,
        'type': 'Electric'
    },

    {
        'name': 'Charmander',
        'power': 'Flamethrower',
        'hp': 39,
        'type': 'Fire'
    }
]

####

# find by name (case-insensitive)
def fibn(array, name):
    for item in array:
        if item['name'].lower() == name.lower():
            return item
    return None

####

class Pokemon:
    def __init__(self, info):
        # info is a dict with name, power, hp, type
        self.name = info['name']
        self.power = info['power']
        self.hp = info['hp']
        self.type = info['type']

    def say_name(self):
        print(self.name)

    # shared battle function
    def attack(self):
        print(self.name + ' used ' + self.power)

####

class Pikachu(Pokemon):
    def __init__(self, info):
        super().__init__(info)

    def special_move(self):
        print(self.name + ' used Volt Tackle!')

####

pikachu_info = fibn(pokemon_data, 'Pikachu')

pikachu = Pikachu(pikachu_info)

pikachu.special_move()

####

"""
Pikachu used Volt Tackle!
"""

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

