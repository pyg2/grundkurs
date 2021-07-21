# wort, zahl
# Hallo mit der Zahl 3 -> Kdoor

def verschluesseln(wort, cypher=3):
    verschluesselt = ''
    ABC = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

    # ..

    # for i in range(len(wort) - 1):

    for buchstabe in wort:
        verschluesselt += ABC[(ABC.find(buchstabe) + cypher) % len(ABC)]

        # neue_pos = pos_in_abc + cypher
        #
        # pos_in_abc = ABC.find(buchstabe)  # Position im Alphabet finden
        # if neue_pos - 1 > len(ABC):
        #     neue_pos = neue_pos % len(ABC)
        #
        # neuer_buchstabe = ABC[neue_pos]
        # verschluesselt += neuer_buchstabe

    return verschluesselt


print(verschluesseln('Python macht Spass', 3))
