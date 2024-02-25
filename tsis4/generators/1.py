def squares(n):
    for i in range(1, n):
        if(i**2 <= n):
            yield i**2

n=int(input())
for a in squares(n):
    print(a)