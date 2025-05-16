# coinflip.py
# Singla slant

import random

def flip():
    return "Krona" if random.randint(0, 1) == 0 else "Klave"

try:
    count = int(input("Hur många gånger vill du singla slant? "))
    if count < 1:
        print("Felaktigt antal.")
        exit()
except ValueError:
    print("Du måste skriva ett heltal.")
    exit()

for _ in range(count):
    print(flip())
