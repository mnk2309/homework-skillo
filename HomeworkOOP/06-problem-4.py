class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = int(self.length * self.width)
        return area

    def perimeter(self):
        perimeter = float(self.length * 2 + self.width * 2)
        return perimeter

    def __eq__(self, other):
        if self.area == other.area:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.perimeter() < other.perimeter()

rect1 = Rectangle(7, 4)
rect2 = Rectangle(10, 5)

print(rect1.__eq__(rect2))
print(rect1.__lt__(rect2))
