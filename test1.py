from polymorphism import Rectangle, Square, Circle

triangle1 = Rectangle(4, 6)
triangle2 = Rectangle(5, 8)
print(triangle1.get_area(), triangle2.get_area())

square1 = Square(4)
square2 = Square(6)
print(square1.get_area(), square2.get_area())

circ1 = Circle(3)
circ2 = Circle(2)
print(circ1.get_area(), circ2.get_area())

figures = [triangle1, triangle2, square1, square2, circ1, circ2]
for figure in figures:
        print(figure.get_area())