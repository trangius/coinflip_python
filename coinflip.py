# coinflip.py
# Singla slant

import random

try:
    count = int(input("Hur många gånger vill du singla slant? "))
    if count < 1:
        print("Felaktigt antal.")
        exit()
except ValueError:
    print("Du måste skriva ett heltal.")
    exit()

for _ in range(count):
    flip = random.randint(0, 1)
    if flip == 0:
        print("Krona")
    else:
        print("Klave")
