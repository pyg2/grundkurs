class Punkt:
    # Eigenschaften
    x = 0
    y = 0

    # Methoden
    def print_info(self):
        # self -> this
        print('X:', self.x, 'Y:', self.y)

    def print_x_mit_text(self, text):
        print(text, self.x)



p1 = Punkt()
p2 = Punkt()

p1.x = 20
p1.y = 22

p2.x = 10
p2.y = 12

# print(p1.x, p1.y)
# print(p2.x, p2.y)
p1.print_info()
p2.print_info()

p1.print_x_mit_text('p1.x ist')
p2.print_x_mit_text('p2.x ist')