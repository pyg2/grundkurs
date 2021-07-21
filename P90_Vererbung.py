class A:
    def __init__(self, zahl):
        self.zahl = zahl
        print('A Konstruktor')

    def print_a(self):
        print('a', self.zahl)


class B(A):  # B(A) -- class B extends A
    def __init__(self):
        super().__init__(42)
        print('B Konstruktor')

    def print_b(self):
        print('b')


class C(B):
    def __init__(self):
        print('hallo')
        super().__init__()
        # super(42)
        print('C Konstruktor')

    def print_b(self):
        print('ÜBERSCHRIEBEN')

    def print_c(self):
        print('c')


# b1 = B()
# b1.print_a()
# b1.print_b()
c1 = C()

# c1.print_c()
# c1.print_b()
c1.print_a()


class D:
    def __init__(self, zahl):
        self.zahl = zahl

    def print_d(self):
        print('d')

class E(D):
    def __init__(self, zahl):
        super().__init__(zahl)


class F(E):
    def __init__(self, zahl):
        super().__init__(zahl)

    def print_d(self):
        print('Überschrieben')
        super().print_d()


f1 = F(22)
f1.print_d()


class G(F, A):
    pass


g1 = G(23)
g1.print_a()