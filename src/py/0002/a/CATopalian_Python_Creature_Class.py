# CATopalian_Python_Creature_Class.py

# base creature data
creature_data = [
    {
        'name': 'Sparkling',
        'power': 'Lightning Burst',
        'hp': 35,
        'type': 'Electric',

        # new property stored directly in the object
        'charge': 100
    },
    {
        'name': 'Flarecub',
        'power': 'Ember Roar',
        'hp': 39,
        'type': 'Fire'
    },
    {
        'name': 'Aqualin',
        'power': 'Tidal Pulse',
        'hp': 47,
        'type': 'Water'
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

class Creature:
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

class Sparkling(Creature):
    def __init__(self, info):
        super().__init__(info)

        # new extended class only properties
        self.charge = info['charge']
        self.electric_affinity = 0.85

    def special_move(self):
        cl(self.name + ' unleashed Thunder Spiral!')

    def use_charge(self):
        # draining charge
        self.charge = self.charge - 10

        cl(self.name + ' now has ' + str(self.charge) + ' charge left')

    def electric_dash(self):
        cl(self.name + ' is Dashing with Current.')

####

# create instance from array data
sparkling_info = fibn(creature_data, 'Sparkling')

sparkling = Sparkling(sparkling_info)

####

# sparkling actions
sparkling.say_name()
sparkling.special_move()
sparkling.use_charge()
sparkling.electric_dash()

####

"""
Sparkling
Sparkling unleashed Thunder Spiral!
Sparkling now has 90 charge left
Sparkling is Dashing with Current.
"""

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

