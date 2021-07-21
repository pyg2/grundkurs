def generiere():
    for i in range(10):
        print('In range', i)
        yield i

generator = generiere()

print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# Geht um 13:30 weiter