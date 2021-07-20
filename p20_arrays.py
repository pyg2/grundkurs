# 0       1         2
namen = ['Tanja', 'Bernd', 'Maria']

print(namen[1])

print(type(namen))

# Ein neues Element einfügen
# JA in Python sind Arrays dynamisch

# NEIN
# namen[3] = 'Karl'
print(namen)

# namen += 'Karl'
namen += ['Karl']
print(namen)

# ODER
namen.append('Jana')
print(namen)

# namen = namen.append('Jana2')
# print(namen)

wort = "hallo"
wort.upper()
print(wort)

# Bei einem STRING muss ich die Rückgabe speichern
wort = wort.upper()
print(wort)

# Sortieren
namen.sort()
print(namen)

namen.sort(reverse=True)
print(namen)

# Element löschen
namen += ['Bernd']
namen.remove('Bernd')

namen.pop(1)  # Zweite Element löschen
print(namen)

print(namen[1])

# Anzahl der Elemente
print(len(namen))

# Coole Sachen (Magic)

print(namen[2:4])
print(namen[-1])

zahlen = [1, 2, 3, 4, 5, 6]

print(zahlen[::2])

print(zahlen[2:4])
print(zahlen[1:4:2])

wort = 'Hallo Welt'
print(wort[::2])

zahlen += [23]


class A:
    def __init__(self, zahl):
        self.zahl = zahl

    def __add__(self, other):
        self.zahl += other


a1 = A(42)

a1 + 3
# a1.__add__(3)

print(a1.zahl)
