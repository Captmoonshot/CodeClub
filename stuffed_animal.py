# stuffed_animal.py

"""A class to simulate robotic stuffed animals."""

class StuffedAnimal:

    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = int(age)
        self.animal_type = animal_type

    # "getters"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_animal_type(self):
        return self.animal_type

    # "setters"

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    # regular methods

    def eat(self, food):
        print(f"{self.name} is eating {food}.  Yummy!")

    def sleep(self):
        print(f"{self.name} is now sleeping...")

    def play(self, game):
        print(f"{self.name} is playing {game}!")

    # special __str__() method to display current state

    def __str__(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Animal type: {self.animal_type}
        """






