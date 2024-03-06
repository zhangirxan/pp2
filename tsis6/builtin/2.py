import functools

s = input()
upper = functools.reduce(lambda x, char: x + 1 if char.isupper() else x, s, 0)
lower = functools.reduce(lambda x, char: x + 1 if char.islower() else x, s, 0)

print("uppers:", upper)
print("lowers:", lower)
