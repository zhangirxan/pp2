import re
file_path = r"C:\Users\zhang\Desktop\pp2\pp2\tsis5\row.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    rows = file.readlines()

for row in rows:
    if re.search("[A-Z]", row):
        words = re.findall("[A-Z][a-z]*", row)
        modified_row = " ".join(words)
        print(modified_row)