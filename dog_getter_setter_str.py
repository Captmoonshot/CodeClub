# dog.py with getters and setters and a __str__ method

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initializes name and age attributes."""
        self.name = name
        self.age = age

    # getter methods for Dog
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # setter methods

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    # regular methods

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")

    # The string method helps us get a nice print out of the instance
    def __str__(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        """

