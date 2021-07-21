class A:
    def __init__(self, zahl):
        self.zahl = zahl

    def __int__(self):
        return self.zahl

    def get_fields(self):
        return (self.zahl)

    # toString()
    def __str__(self):
        return 'Zahl ist ' + str(self.zahl)

    # def __dir__(self):
    #     return {}

    def __iter__(self):
        return iter([1, 2, 3])


    def get_dict(self):
        return {'zahl': self.zahl}

a1 = A(42)

print(int(a1))

print(a1)
# print(str(a1))

# print(dict(a1))
# print(dir(a1))
#
# import math
#
# print(dir(math))

# print(dict(a1))

kunde = {
    'vorname': 'Maria',
    'nachname': 'Huber',
}

for k in kunde:
    print(k)

# for a in a1.get_fields():
#     print(getattr(a1, a))

for a in a1:
    print(a)


keine_schleife = [1, 2, 3]  # -> iterrierbar
iterator = iter(keine_schleife)  # -> iterator

print(next(iterator))
print(next(iterator))
print(next(iterator))

bla = {'vorname': 'Bernd', 'nachname': 'Huber'}
bla_iterator = iter(bla)

print(next(bla_iterator))

# test = dict(bla_iterator)

# print(test)

print(vars(a1))
