class AddClass:
    def __init__(self, zahl):
        self.zahl = zahl

    def __add__(self, other):
        ## Magische Methoden
        # fangen mit __ an und enden mit zwei __
        self.zahl += other
        return self

    def __sub__(self, other):
        if isinstance(other, AddClass):
            self.zahl -= other.zahl
            return self

        if not isinstance(other, int):
            print('Bitte nur Zahlen')
            return self

        self.zahl -= other
        return self


a1 = AddClass(20)

a1 + 3
# a1.__add__(3)  # Nicht der typsiche Aufruf

print(a1.zahl)

a1 - 6

print(a1.zahl)

a1 - 'asdf'

a2 = AddClass(20)

a1 - a2

print(a1.zahl)


# a1 + 20 + 20
#
# print(a1.zahl)

a1 = a1 + 20
print(a1.zahl)


class Chaining:
    def __init__(self):
        self.__background = ''
        self.__color = ''
        self.__border = ''

    def set_background(self, background):
        self.__background = background
        return self

    def set_color(self, color):
        self.__color = color
        return self

    def set_border(self, border):
        self.__border = border
        return self

    def print_info(self):
        print(self.__background, self.__color, self.__border)


c1 = Chaining()
# c1.set_background('grün')
# c1.set_color('weiß')
# c1.set_border('schwarz')

c1.set_background('grün').set_color('weiß').set_border('schwarz')

print(c1.print_info())