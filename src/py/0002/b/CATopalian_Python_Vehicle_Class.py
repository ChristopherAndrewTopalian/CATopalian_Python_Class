# CATopalian_Python_Vehicle_Class.py

# base vehicle data
vehicle_data = [
    {
        'name': 'RoadRunner',
        'power': 'Turbo Boost',
        'hp': 170,
        'type': 'Car',

        # new property
        'fuel': 100
    },
    {
        'name': 'IronHauler',
        'power': 'Heavy Pull',
        'hp': 250,
        'type': 'Truck',
        'fuel': 180
    }
]

####

# shortcuts

def cl(message):
    print(message)

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
        # base properties
        self.name = info['name']
        self.power = info['power']
        self.hp = info['hp']
        self.type = info['type']

    def identify(self):
        cl('this is ' + self.name)

    def use_power(self):
        cl(self.name + ' activated ' + self.power)

####

class Car(Vehicle):
    def __init__(self, info):
        super().__init__(info)

        # new extended class properties
        self.fuel = info['fuel']
        self.traction = 0.85

    def drift(self):
        cl(self.name + ' performed a drift!')

    def use_fuel(self):
        self.fuel = self.fuel - 10
        cl(self.name + ' now has ' + str(self.fuel) + ' fuel left')

    def turbo_dash(self):
        cl(self.name + ' dashed forward with turbo!')

####

# create instance
roadrunner_info = fibn(vehicle_data, 'RoadRunner')

roadrunner = Car(roadrunner_info)

####

# actions
roadrunner.identify()
roadrunner.use_fuel()
roadrunner.drift()
roadrunner.turbo_dash()

####

"""
this is RoadRunner
RoadRunner now has 90 fuel left
RoadRunner performed a drift!
RoadRunner dashed forward with turbo!
"""

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

