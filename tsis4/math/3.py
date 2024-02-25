import math
def regular_polygon_area(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
area = regular_polygon_area(sides, length)
print("The area of the polygon is:", area)
