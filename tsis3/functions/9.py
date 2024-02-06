import math
def func(r):
    volume = (4/3) * (math.pi) * r*r*r
    return volume
radius=float(input())
print(func(radius))
