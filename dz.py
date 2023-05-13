#2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
a = Rectangle(5, 10)
print(a.area())
print(a.perimeter())
b = Rectangle(6, 9)
print(b.area())
print(b.perimeter())
