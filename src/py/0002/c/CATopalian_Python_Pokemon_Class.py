# CATopalian_Python_Pokemon_Class.py

# base pokemon data
pokemon_data = [
    {
        'name': 'Pikachu',
        'power': 'Thunderbolt',
        'hp': 35,
        'type': 'Electric',

        # new property
        'stamina': 100
    },
    {
        'name': 'Charmander',
        'power': 'Flamethrower',
        'hp': 39,
        'type': 'Fire',
        'stamina': 95
    }
]

####

# shortcuts

def cl(message):
    print(message)

####

# find item by name (case insensitive)
def fibn(array, name):
    for item in array:
        if item['name'].lower() == name.lower():
            return item
    return None

####

class Pokemon:
    def __init__(self, info):
        # base properties
        self.name = info['name']
        self.power = info['power']
        self.hp = info['hp']
        self.type = info['type']

    def say_name(self):
        cl(self.name)

    def attack(self):
        cl(self.name + ' used ' + self.power)

####

class Pikachu(Pokemon):
    def __init__(self, info):
        super().__init__(info)

        # new extended class properties
        self.stamina = info['stamina']
        self.electricSkill = 0.92

    def special_move(self):
        cl(self.name + ' used Volt Tackle!')

    def use_stamina(self):
        self.stamina = self.stamina - 15
        cl(self.name + ' now has ' + str(self.stamina) + ' stamina left')

    def spark_dash(self):
        cl(self.name + ' dashed with sparks!')

####

# create instance from data
pikachu_info = fibn(pokemon_data, 'Pikachu')

pikachu = Pikachu(pikachu_info)

####

# actions
pikachu.say_name()
pikachu.attack()
pikachu.use_stamina()
pikachu.spark_dash()
pikachu.special_move()

####

"""
Pikachu
Pikachu used Thunderbolt
Pikachu now has 85 stamina left
Pikachu dashed with sparks!
Pikachu used Volt Tackle!
"""

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

