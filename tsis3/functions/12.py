def histrogram(x):
    for i in x:
        print('*' * i)
str1 = input()
x = [int(i) for i in str1.split()]
histrogram(x)