from sys import argv

script, first, second, third = argv

print()  # The empty print statements make the output neater
print(f"The program name is: {script}")
print(f"The first variable is: {first}")
print(f"The second variable is: {second}")
print(f"The third variable is: {third}")
print()
print()
"""
A question you might have have about ex13.py might be:

How exactly does unpacking work?  In other words, how are the arguments
that we pass from the Terminal like "cheese", "fries", "burger" getting unpacked
into the individual variables?

Try this exercise
"""

# First, what type of object is argv?
# Let's find out
what_is_argv = type(argv)    # Remember what type does?
print(f"argv is: {what_is_argv}")
print()

# argv is a LIST
# We haven't gone over lists yet, but we will!

# So how do lists unpack things?

# Try this
print("""The following creates a list name my_list and unpacks the items
into different variables.""")
print()
my_list = ["cheese", "fries", "drink", "burger"]
print(f"My list: {my_list}")
print()
print("Now we unpack the items into different variables.")
print()
var1, var2, var3, var4 = my_list
print("Printing items:")
print(var1)
print(var2)
print(var3)
print(var4)







