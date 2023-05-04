"""randomly generate funny nicknames."""

import sys
import random
print("Welcome to the YellowJackets 'Random Name Picker.'\n")

print("nothing tired , nothing old, here is the name for you: \n\n")

first = ('Snackie', 'CitzenDetective', 'Cannibal', 'GreyGoose', 'AfricanGrey', 'Javi',
         'noSteve','ShaunBright','Heisty','Sleepwalk Tai')
last = ('Yum', 'Woods', 'Crash', 'Plane', 'Desire', 'Attic', 'Nightmare','Dammit Randy'
        ,'LastResort', 'Burn')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n")
    print("{} {}".format(firstName,lastName),file = sys.stderr)
    print("\n\n")

    try_again = input("\nTry Again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break
input ("\n Press Enter to exit.")
