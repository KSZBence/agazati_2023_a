import random


def szam():
    szam = random.randint(1, 50)
    print(f"I/A:\n\tA generált szám: {szam}\nI/B:")
    if szam % 3 == 0 and szam % 5 == 0:
        print("\tA szám öttel és hárommal is osztható!")
    elif szam % 3 == 0:
        print("\tA szám hárommal osztható!")
    elif szam % 5 == 0:
        print("\tA szám öttel osztható!")

