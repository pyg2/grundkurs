def change_zahl(zahl):
    # zahl ist eine LOKALE Variable
    # mit dem (kopierten) Wert 42
    zahl = 23


zahl = 42

change_zahl(zahl)

print(zahl)


def change_string(wort):
    # EINE KOPIE
    wort = 'welt'


wort = 'hallo'

change_string(wort)

print(wort)


def change_namen(namen):
    # REFERENZEN
    namen[1] = 'GEÄNDERT'


namen = ['Bernd', 'Tanja', 'Maria']

change_namen(namen)

print(namen)

z1 = [2, 3, 4]
z2 = z1

z2[1] = 42

print(z1)
print(id(z1), id(z2))

i1 = 3
i2 = i1
i2 = 42

print(i1)  # 3


"""
Primitive Datentypen (int, float, bool) + String
 -> werden KOPIERT
Komplexe Datentypen (Array, Dictionaries, Objekte)
 -> werden REFERENZIERT (e.g. selber Speicherbereich)


"""

