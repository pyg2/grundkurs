# Vergleichsoperatoren
# == != > < >= <=

print(42 == 42)
print(42 != 42)

# Merke: Vergleichsoperatoren überprüfne auch den DATENTYP
print(42 == '42')

# Logischen Operatoren
# &&
"""
true and true = true
false and true = false
true and false = false
false and false = false
"""
print(42 == 42 and 42 < 23)

# ||
# or

"""
true and true = true
false and true = true
true and false = true
false and false = false
"""

print(42 == 42 or 42 < 23)

# Logische nicht (!)

print(not True)
print(not False)

zahl = 42

if not zahl:
    print('Zahl ist 0 oder None etc.')


if 10 < zahl < 100:
    print('Zahl ist zwischen 11 und 99')
