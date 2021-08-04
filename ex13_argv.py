# ex13.py
# by Zed Shaw

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print()
what_is_argv = type(argv)
print(f"argv is: {what_is_argv}")
print()

