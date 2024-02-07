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
number = int(input())
if prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")