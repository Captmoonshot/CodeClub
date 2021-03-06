# dog.py
# by Eric Matthes

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initializes name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")






