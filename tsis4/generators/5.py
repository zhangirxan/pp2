def rev(n):
    while n >= 0:
        yield n
        n-=1
n=int(input())
for num in rev(n):
    print(num)