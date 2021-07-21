import mod.modul1
# from mod.modul1 import *  # Schlechter Stil
from mod.modul1 import zahl, zahl2  # Besser
import random
import math

from random import random

from math import pi

import A

from A import A


print('Hallo aus dem Hauptprogramm')
print(mod.modul1.zahl)
print(zahl)
print(mod.modul1.zahl2)
print(zahl2)

math.pi = 2323

print(math.pi)
# print(random.random())
# a1 = A.A()
# a1 = A()
A.a()