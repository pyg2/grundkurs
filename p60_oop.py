# Kunde: Bernd Huber 42

kunden_als_liste = ['Bernd', 'Huber', 42]
kunden_als_liste2 = ['Bernd', 'Huber', 'Musterstr. 42', 42]

print(kunden_als_liste[2])

"""
Nachteil:

- Merken an welcher Stelle etwas steht
- Kein Formatzwang
"""

kunde_als_dict = {
    'vorname': 'Bernd',
    'nachname': 'Huber',
    'alter': 42,
}

print(kunde_als_dict['alter'])

"""
Nachteile:

- Kein Formatzwang
- Einheitlich
"""


class Kunde:
    # Template / Vorlage
    # Eigenschaften / Attribute / Properties
    # Instanzvariablen
    vorname = ''
    nachname = ''
    alter = 0
    strasse = ''
    ort = 'Deutschland'


kunde_als_objekt = Kunde()

kunde_als_objekt.vorname = 'Bernd'
kunde_als_objekt.nachname = 'Huber'
kunde_als_objekt.alter = 42

k2 = Kunde()
k2.vorname = 'Maria'
k2.nachname = 'Huber'
k2.alter = 44


print(kunde_als_objekt.alter)
print(k2.alter)
print(kunde_als_objekt.ort)
print(k2.ort)

"""
public class Kunde {
    public String vorname;
    public String nachname;
    public byte alter;    
}

Kunde kunde_als_objekt = new Kunde();


"""
