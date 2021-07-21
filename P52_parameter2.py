def addiere(zahl1, zahl2, zahl3=0):
    return zahl1 + zahl2 + zahl3


print(addiere(20, 22))
print(addiere(20, 12, 10))


def subtrahiere(zahl1, zahl2, zahl3=0, zahl4=0):
    return zahl1 - zahl2 - zahl3 - zahl4


# print('text1', 42, sep=',')

subtrahiere(22, 10, zahl4=12)


def print_anschrift(vorname, nachname, anrede='Sehr geehrte/r', ort='Deutschland'):
    print(anrede, nachname, 'aus', ort)


print_anschrift('Bernd', 'Müller')
print_anschrift('Bernd', 'Müller', ort='Schweiz')
print_anschrift('Bernd', 'Müller', anrede='Sehr geehrter Herr', ort='Schweiz')



# Mittagspause bis 13:40 :-)

