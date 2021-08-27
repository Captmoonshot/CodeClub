# ex31.py
# by Zed Shaw

print("""You enter a dark room with three doors.
Do you go through door #1 or door #2 or door # 3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("""An kid named Morty and a pickle named Pickle Rick show up help.
    They offer you two choices.""")
    print("1. Refuse their help.")
    print("2. Take the red pill and wake up from this horrible nightmare.")

    choice = input("> ")

    if choice == "1":
        print("You offended them, so Rick and Morty turned you into a pickle.")
    else:
        print("Your mom wakes you up to a nice breakfast of pancakes and strawberries.")

    





