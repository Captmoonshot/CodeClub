import random

def generate_random_number():
    """This function generates a random number
    in the range 0 to 10 inclusive of the 10."""
    random_number = random.randint(0, 10)
    return random_number

def random_sentence():
    number_one = generate_random_number()
    number_two = generate_random_number()
    number_three = generate_random_number()
    print(f"I have {number_one} dollars in my bank account.")
    print(f"I have {number_two} friends at school.")
    print(f"I got a {number_three} out of 10 on my math test.")













