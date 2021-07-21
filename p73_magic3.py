class A:
    test = 22

    def __getattr__(self, item):
        return 42


a1 = A()
print(a1.zahl)
print(a1.asdf)
print(a1.test)

print(hasattr(a1, 'asdf'))