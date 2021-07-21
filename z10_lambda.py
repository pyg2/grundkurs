def verdoppeln_als_funktion(x):
    return x * 2


verdoppeln = lambda x: x * 2

print(verdoppeln(2))


addiere = lambda zahl1, zahl2: zahl1 + zahl2


def rufe_funktion_auf(func):
    return func(2) * 2


print(rufe_funktion_auf(lambda x: x * 3))


# 2 * 3 * 2