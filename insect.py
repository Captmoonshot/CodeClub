# insect.py

"""The Insect class holds general data about insects."""

class Insect:

    def __init__(self, insect_type, fly, pollinate):
        self.insect_type = insect_type
        self.fly = fly
        self.pollinate = pollinate

    # getters

    def get_insect_type(self):
        return self.insect_type

    def get_fly(self):
        return self.fly

    def get_pollinate(self):
        return self.pollinate

    # setters

    def set_insect_type(self, insect_type):
        self.insect_type = insect_type

    def set_fly(self, fly):
        self.fly = fly

    def set_pollinate(self, pollinate):
        self.pollinate = pollinate

    # to display current state of the Insect instance
    def __str__(self):
        return f"""
        Type: {self.insect_type}
        Fly: {self.fly}
        Pollinate: {self.pollinate}
        """

"""The Bee class will hold data about bees and will inherit from the Insect class"""

class Bee(Insect):

    def __init__(self, insect_type, fly, pollinate, sting):
        super().__init__(insect_type, fly, pollinate)

        self.sting = sting

    def get_sting(self):
        return self.sting

    def set_sting(self):
        self.sting = sting

    def __str__(self):
        return f"""
        Type: {self.insect_type}
        Fly: {self.fly}
        Pollinate: {self.pollinate}
        Sting: {self.sting}
        """







