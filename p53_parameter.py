print('hallo', 'welt', 'Bernd', sep='----')


# int[] args

# In Python dafür *qwargs
def addiere(*zahlen, rechen_art='+'):
    erg = 0

    for z in zahlen:
        erg += z

    return erg


print(addiere(20, 22))  # [20, 22]-> zahlen
print(addiere(20, 22, 10, rechen_art='-'))


def addiere2(*zahlen):
    return sum(zahlen)


def print_kunde(nachname, **daten):  # {'strasse': '...'}
    print('Nachname', nachname)
    print('Strasse', daten.get('strasse', ''))
    print('PLZ', daten.get('plz', ''))
    print('Ort', daten.get('ort', 'München'))


print_kunde('Huber', strasse='Musterstr. 42', plz='11232', ort='Berlin')


import logging

logging.basicConfig(filename='test.log', level=logging.INFO)



print(sum([2, 3 ,4]))


