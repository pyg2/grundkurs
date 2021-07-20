# Aufgabe: Gebt die ersten 1000 Primzahlen aus

"""
WICHTIG, Aufgabe teilen:

- Wie finde Ich heraus ob eine beliebige Zahl eine Primzahl ist
"""
count = 0
zahl = 3

# for (int i = 2; i < zahl; i++)

while count < 1000:
    is_prime = True

    for i in range(2, zahl):
        if zahl % i == 0:
            is_prime = False
            break

    if is_prime:
        print(zahl, end=', ')
        count += 1

        if count % 20 == 0:
            print('')

    zahl += 1

