import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x = float(input())
y = float(input())
point1 = Point(x, y)

point1.show()

new_x = float(input())
new_y = float(input())
point1.move(new_x, new_y)

point1.show()

x2 = float(input())
y2 = float(input())
point2 = Point(x2, y2)

distance = point1.dist(point2)

print(distance)
