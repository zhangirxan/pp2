import os
path = r"C:\\Users\\zhang\\Desktop\\pp2\\pp2\\tsis6\\exz\abc.txt"

with open(path, 'r') as file:
    line_count = sum(1 for line in file)

print(f'number of lines in a file: {line_count}') 