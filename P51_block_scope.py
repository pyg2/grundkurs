def scope():
    # Lokale Variable
    zahl = 42
    # Gilt bis zum Ende des Blocks

scope()

# print(zahl)


if True:
    zahl = 42


print(zahl)

"""
// short zahl = 0;

if (true) {
    short zahl = 42;
}

print(zahl);
"""

# for (int i = 0; i < 10; i++) {
#   Nur hier gibts i
# }
for i in range(10):
    test = 42

print(i)
print(test)
