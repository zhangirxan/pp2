from itertools import permutations
def func(str):
    perms = permutations(str)
    for perm in perms:
        print(''.join(perm))

str1 = input()
func(str1)
