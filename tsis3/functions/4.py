def filter_prime(lst):
    prime_numbers = []
    for num in lst:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers

input_numbers = input("vvedite list").split()
lst = [int(num) for num in input_numbers]
prime_numbers = filter_prime(lst)
print( prime_numbers)
