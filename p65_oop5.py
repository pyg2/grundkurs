class Auto:
    cnt = 0

    def __init__(self, ps):
        Auto.cnt += 1
        self.ps = ps

    # public static void increase_cnt()
    @staticmethod
    def increase_cnt():
        # self.ps = 999
        Auto.cnt += 1


a1 = Auto(42)   # Counter der Klasse erhöht um 1 Auto.cnt += 1
print(a1.ps)

a2 = Auto(33)  # Counter der Klasse erhöht um 1 -> 2

print(a1.cnt)  # nicht sauber
print(a2.cnt)
print(Auto.cnt)

a3 = Auto(44)

print(Auto.cnt)

Auto.increase_cnt()
print(Auto.cnt)

# Math.random()

"""
class Math {
    public static double random() {
        return 0.42;
    }
}

Math.random(); // Weil es statisch ist

Math m = new Math()
m.random();
"""


class Auto:
    def __init__(self, hersteller):
        self.hersteller = hersteller

    def fahren(self):
        return 42


auto1 = Auto('VW')
auto2 = Auto('Renault')
auto3 = Auto('Citreon')
auto4 = Auto('BMW')

autos = [auto1, auto2, auto3, auto4]

del auto1
del auto2
del auto3
del auto4

# print(auto1)

"""
autos = [
    Auto(hersteller: 'VW'),
    Auto(hersteller: 'Renault'),
    ..


}
"""

print(autos[2])

loeschen = 'BMW'

for auto in autos:
    if auto.hersteller == loeschen:
        autos.remove(auto)
        break


for auto in autos:
    print(auto.hersteller)

