import math
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2
    
length = float(input())
obj_square = Square(length)
area = obj_square.area()
print(area)
