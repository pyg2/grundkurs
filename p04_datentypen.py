# Kommazahlen

pi = 3.1415925

print(1.12345678901234567890)
print(4.12345678901234567890)

print(0.5 + 0.5)
print(0.5 + 0.3 + 0.2)
print(0.5 + 0.2 + 0.2 + 0.1)
print(0.5 + 0.2 + 0.1)

print(12312312312312313123.123)
print(type(pi))

print('-------------------')

# IN Python gibt es keinen char Datentyp (immer String)
print(type('a'))
print(type('hallo welt'))

print(chr(97))

# Boolean
wahr = True
falsch = False

print(type(wahr))

if 42:
    print('42 ist wahr')


# int zahl;
# String wort = null;

# False: 0, '', False, None, []
# True:
# * True
# * Jede Zahl, ausser die 0
# * JEder String, ausser ein leerer String ist wahr ('')


if -1:
    print('-1 ist wahr')

if 'hallo':
    print('hallo ist wahr')

if '':
    print('Leerer String ist afalsch')

if None:
    print('None')

print(type(None))

# String[] namen = {};
namen = []

if namen:
    print('Namen ist False')

wort = 'hallo'

print(type(namen))

dictionaries = {
    'vorname': 'Bernd',
    'nachname': 'Huber'
}

print(dictionaries['vorname'])
print(type(dictionaries))

unveraenderlich = ('Bernd', 'Maria', 'Tanja')

print(type(unveraenderlich))

print('----------')


class Kunde:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname


print(type(Kunde))

# new Kunde()
bernd = Kunde('Bernd', 'Huber')

print(type(bernd))

# void print_hello() {
#   printf("Hallo");
# }


def print_hallo():
    print('Hallo')


print(type(print_hallo()))
print(type(print_hallo))

print('-----')

import math

print(type(math))

print(42 == '42')






