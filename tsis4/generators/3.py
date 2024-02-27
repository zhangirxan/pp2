def func(n):
    for i in range(n):
        if(i % 3 == 0 and i % 4 == 0):
            yield i
n=int(input())
for value in func(n):
    print(value)