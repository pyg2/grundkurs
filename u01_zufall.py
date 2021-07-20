from random import random

# print(random())

# Aufgabe: Mit 42% Wahrscheinlichkeit gewonnen ausgeben

zufall = random()

if zufall < 0.42:
    print('Gewonnen')

