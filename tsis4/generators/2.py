def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield str(i)

n = int(input())
a = ", ".join(even(n))
print(a)