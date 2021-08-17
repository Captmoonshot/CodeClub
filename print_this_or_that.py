# print_this_or_that.py
# Sammy Lee

"""The following function will randomly pick a statement to print"""

import random

def print_random_stuff(*args):
    statements = list(args)
    random_statement = random.choice(statements)
    print(random_statement)


# print_random_stuff("I love Miraculous", "I love Mac n Cheese", "I love Python", "I love Math")


# for i in range(0, 10):
#     print_random_stuff("I love Miraculous", "I love Mac n Cheese", "I love Python", "I love Math")

"""How do we really know this is random? We would know if ran the program many, many
times and counted the number of times each random statement occurred.  If they occur a 
similar number of times then most likey they are random occurrences.  Here we choose a statement
one million times, put them in a list and count the occurrences of each statement."""

# from collections import Counter

# def print_random_stuff_and_count(*args):
#     statements = list(args)
#     random_list = []
#     for i in range(1000000):
#         random_statement = random.choice(statements)
#         random_list.append(random_statement)
#     print(Counter(random_list))




