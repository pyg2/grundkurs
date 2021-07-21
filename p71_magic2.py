class Kunde:
    def __init__(self, kunden_nummer):
        self.kunden_nummer = kunden_nummer

    def __eq__(self, other):
        if not isinstance(other, Kunde):
            return

        return other.kunden_nummer == self.kunden_nummer

    def __lt__(self, other):
        # lt, gt, ge, le, eq, ne
        # <  >  >=  <= == !=
        return self.kunden_nummer < other.kunden_nummer




k1 = Kunde(1000)
k2 = Kunde(1000)
k3 = Kunde(1001)

print(k1 == k2)
print(k1 == k3)

print(k1.kunden_nummer == k2.kunden_nummer)

print(k1 < k3)
