# for und while

# for ist in Python ein Iterator

# for (int i = 0; i < 10; i++)

# for each for (int zahl : zahlen)
for i in [0, 1, 2, 3, 4, 5]:
    i += 10
    print(i)

for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

print(range(10))

for name in ['bernd', 'Maria', 'tanja']:
    print(name)

namen = ['bernd', 'Maria', 'tanja']

for name in namen:
    print(namen)


iterator = iter(namen)

print(next(iterator))
print(next(iterator))
print(next(iterator))


