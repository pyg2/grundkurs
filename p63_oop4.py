"""
class Auto {
    public int ps = 0;
}

Auto a1 = new Auto();
a1.ps = 232;

class Auto2 {
    private int ps = 0;
}

Auto2 a2 = new Auto2();
a2.ps = 232;  # Fehler
"""


class Auto:
    def __init__(self):
       self.__ps = 0

    def set_ps(self, ps):
        if ps > 1000:
            # throw new Exception("glaub ihc nicht")
            raise ValueError('Glaub ich nicht')

        self.__ps = ps

    def get_ps(self):
        return str(self.__ps) + ' PS'

a1 = Auto()
# a1.ps = 3999099
# a1._protected = 9999999
# a1.__privat = 42

# class mangeling
# print(a1._Auto__privat)
# print(a1.__privat)

a1.set_ps(42)
print(a1.get_ps())

a1.set_ps(9999)
print(a1.get_ps())
