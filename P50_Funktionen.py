"""
Funktionen
- Übersichtlichkeit
- Wiederverwendbarkeit (DRY)
- Testbarkeit
"""


# Reihenfolge beachten
# print_hello()

def print_hallo():
    print('hallo')
    # SOlange die Einrückung besteht
    # hier ist die Funktion


# Ausserhalb der Funktion


print_hallo()
print_hallo()
print_hallo()
print_hallo()

print(type(print_hallo))

# Parameter

"""
public static void addiere(int zahl1, int zahl2) {
    System.out.println(zahl1 + zahl2);
}

"""


def addiere(zahl1, zahl2):
    if not isinstance(zahl1, int) \
        or isinstance(zahl2, int):
        print('Fehler')
        return

    print(zahl1 + zahl2)


def addiere2(zahl1: int, zahl2: int):
    print(zahl1 + zahl2)


addiere(23, 19)
# addiere('23', 19)
addiere2('23', '23')


# Rückgabe

def get_sinn():
    """
    Ermittelt den SInn
    :return:
    """
    return 42
    print('asdf')


get_sinn()


def is_sinn(zahl):
    if zahl == 42:
        return True

    if zahl == 666:
        # Nur einen Datentyp zurückgeben
        # return 'Hilfe'
        # throw new Exception
        raise ValueError('HILFE!')

    return False


is_sinn(42)


def get_ergebnis_addition(zahl1, zahl2):
    return int(zahl1 + zahl2)


def get_ergebnis_addition_und_subtraktion(zahl1, zahl2):
    return [(zahl1 + zahl2), (zahl1 - zahl2)]


ergebnis = get_ergebnis_addition_und_subtraktion(20, 22)

print(ergebnis[0])
print(ergebnis[1])


def get_ergebnis_addition_und_subtraktion2(zahl1, zahl2):
    return {
        'addition': (zahl1 + zahl2),
        'subtraktion': (zahl1 - zahl2),
        'division': (zahl1 / zahl2),
        'multiplikation': (zahl1 * zahl2),
    }


ergebnis2 = get_ergebnis_addition_und_subtraktion2(20, 22)

print(ergebnis2['addition'])
print(ergebnis2['subtraktion'])

# Globale Variablen
ergebnis_addition = 0
ergebnis_subtraktion = 0


def get_ergebnis_addition_und_subtraktion3(zahl1, zahl2):
    # Lokale Variablen
    global ergebnis_addition, ergebnis_subtraktion
    ergebnis_addition = zahl1 + zahl2
    ergebnis_subtraktion = zahl1 - zahl2


get_ergebnis_addition_und_subtraktion3(20, 22)

print(ergebnis_addition)
print(ergebnis_subtraktion)


global_zahl = 42


def global_test():
    # global global_zahl
    print(global_zahl)
    # global_zahl = 23


global_test()


