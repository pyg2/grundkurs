from random import random

"""
class Auto {
    public Auto() {
    }
}
"""


class Auto:
    # Konstruktor
    def __init__(self, hersteller, modell, ps, farbe='schwarz'):
        # Eigenschaften IMMER im Konstruktor
        self.hersteller = hersteller
        self.modell = modell
        self.ps = ps
        self.farbe = farbe

        # Methode die beim instanzieren der Klasse (a1 = Auto()) aufgerufen wird
        print('Konstruktor wird aufgerufen')

    # Methoden
    def fahren(self):
        return self.ps * random()


passat = Auto('VW', 'Passat', 130)

c3 = Auto('Citroen', 'c3', 80, 'mint')

zoe = Auto('Renault', 'Zoe', 80, 'weiß')

# Geht nicht mehr
# nix = Auto()


print(passat.fahren())
print(c3.fahren())
print(zoe.fahren())
# print(nix.fahren())

# Bitte nicht!
# passat.was_neues = 42
# print(passat.wasneues)

