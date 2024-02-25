import math

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
length = float(input())
obj_square = Square(length)
area = obj_square.area()
print(area)
