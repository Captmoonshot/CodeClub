# ex38.py
# by Zed Shaw

ten_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee",
    "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(" ".join(stuff)) # what? cool!
print("#".join(stuff[3:5])) # super stellar!







