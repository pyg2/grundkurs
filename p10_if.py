zahl = 666

"""
if (zahl == 42) {
    ...
}

"""

if zahl == 42:
    print('Du hast den Sinn gefunden')
    print('Wird auch bei 42 ausgegeben')
elif zahl == 666:
    # Reihenfolge beachten
    print('?!?!')
elif zahl > 100:
    print('Life is simple')
else:
    print('Du bist noch auf der Suche')

print('Wird immer ausgegeben')
