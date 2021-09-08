# superhero.py

class SuperHero:

    def __init__(self, first, last, superpower):
        self.first = first
        self.last = last
        self.superpower = superpower

    def get_superpower(self):
        return self.superpower

    def set_superpower(self, superpower):
        self.superpower = superpower

    def use_superpower(self):
        print(f"I've used my {self.superpower} against you!")
        print("Prepare to lose!")






