import math
#1
class salamaleikum:
    def __init__(salam):
        salam.s = ""

    def getString(salam):
        salam.s = input()

    def printString(salam):
        print(salam.s.upper())
#2
class Shape:
    def __init__(salam):
        pass
    
    def area(salam):
        return 0

class Square(Shape):
    def __init__(salam, length):
        super().__init__()
        salam.length = length
    
    def area(salam):
        return salam.length ** 2
#3
class Rectangle(Shape):
    def __init__(salam, length, width):
        super().__init__()
        salam.length = length
        salam.width = width
    
    def area(salam):
        return salam.length * salam.width
#4
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
#5
class Account:
    def __init__(salam, owner, balance=0):
        salam.owner = owner
        salam.balance = balance

    def deposit(salam, summa):
        print("Your balance:", salam.balance)
        if summa >= 0:
            salam.balance += summa
            print("Your Balance:", salam.balance)
        else:
            print("Rewrite input")

    def withdraw(salam, summa):
        print("Your balance:", salam.balance)
        if 0 <= summa <= salam.balance:
            salam.balance -= summa
            print("Withdrawal:", summa)
            print("Balance:", salam.balance)
        else:
            print("You don't have enough")
#6
def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True








