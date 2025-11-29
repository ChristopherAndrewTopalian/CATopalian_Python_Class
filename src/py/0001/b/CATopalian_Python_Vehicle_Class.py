# CATopalian_Python_Vehicle_Class.py

# vehicle data list
vehicle_data = [
    {
        'name': 'RoadRunner',
        'power': 'Turbo Boost',
        'hp': 170,
        'type': 'Car'
    },

    {
        'name': 'IronHauler',
        'power': 'Heavy Pull',
        'hp': 250,
        'type': 'Truck'
    }
]

####

# find by name (case insensitive)
def fibn(array, name):
    for item in array:
        if item['name'].lower() == name.lower():
            return item
    return None

####

class Vehicle:
    def __init__(self, info):
        # info has name, power, hp, type
        self.name = info['name']
        self.power = info['power']
        self.hp = info['hp']
        self.type = info['type']

    def identify(self):
        print('this is ' + self.name)

    def use_power(self):
        print(self.name + ' activated ' + self.power)

####

class Car(Vehicle):
    def __init__(self, info):
        super().__init__(info)

    def drift(self):
        print(self.name + ' performed a drift!')

####

class Truck(Vehicle):
    def __init__(self, info):
        super().__init__(info)

    def haul(self):
        print(self.name + ' hauled a heavy load!')

####

roadrunner_info = fibn(vehicle_data, 'RoadRunner')

roadrunner = Car(roadrunner_info)

roadrunner.drift()

####

"""
RoadRunner performed a drift!
"""

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

