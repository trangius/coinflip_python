# coinflip.py
# Singla slant

import random

count = int(input("Hur många gånger vill du singla slant? "))
for _ in range(count):
    flip = random.randint(0, 1)
    if flip == 0:
        print("Krona")
    else:
        print("Klave")
