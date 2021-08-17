# print_this_or_that.py
# Sammy Lee

"""The following function will randomly pick a statement to print"""

import random

def print_random_stuff(*args):
    statements = list(args)
    random_statement = random.choice(statements)
    print(random_statement)



# print_random_stuff("I love Miraculous", "I love Mac n Cheese", "I love Python", "I love Math")

for i in range(0, 10):
    print_random_stuff("I love Miraculous", "I love Mac n Cheese", "I love Python", "I love Math")


