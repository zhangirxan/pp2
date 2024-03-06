import functools

s = input("введите как [1,2,3..]  ")
l1st = eval(s) 
print(functools.reduce(lambda x, y: x*y, l1st))