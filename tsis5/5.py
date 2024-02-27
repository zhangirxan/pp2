import re
file_path = r"C:\Users\zhang\Desktop\pp2\pp2\tsis5/row.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    rows = file.readlines()

for row in rows:
    if re.findall("a[a-zA-Z]b$", row):
        print(row.strip())