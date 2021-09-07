# ex40b.py

"""A class to hold contact information on an iPhone"""

class Contact:

    # The __init__ method helps to create the object by defining their attributes
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    # These are called "getter" methods

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
    
    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email

    # These are called "setter" methods

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_phone_number(self, phone_number):
        self.phone_number

    def set_email(self, email):
        self.email = email

    def call_contact(self):
        print(f"Calling {self.phone_number}...")

    # The __str__ method returns the object's current state as a string
    def __str__(self):
        return f"""
        Name: {self.first_name} {self.last_name}
        Phone: {self.phone_number}
        Email: {self.email}
        """





