# Operatoren

# Verknüpfungsoperator
print("Hallo" + " " + "Welt")

# Zuweisungsoperator
zahl = 42

# Rechenoperatoren
# +-*/

# Modulo (Die Frage nach dem Rest)
print(11 % 4)
print(12 % 4)

# Ist eine Zahl gerade oder ungerade?
print(10 % 2)
print(11 % 2)

# Ist eine Zahl teibar durch?

print(42 % 100)
print(142 % 100)
print(242 % 100)

for i in range(100):
    if i % 20 == 0:
        print('Alle 20 Durchläufe')

# Inkrementoren / Dekrementoren
# gibt es in Python NICHT
i = 0
# print(i++) i++ ++i i-- --i

# Kurzformen
i = i + 1

i += 1
i *= 2  # i = i * 2

# += *= /= -= %=

print(2 ** 8)

print(11 / 3)

# Flooring
print(11 // 3)
print(int(3.999))
print(round(3.999))
