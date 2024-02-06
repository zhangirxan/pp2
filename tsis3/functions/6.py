def func(str):
  words = str.split()
  rev_str = ' '.join(reversed(words))
  return rev_str

str1 = func(input())
print(str1)