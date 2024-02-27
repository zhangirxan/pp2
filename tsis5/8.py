import re
file_path = r"C:\Users\zhang\Desktop\pp2\pp2\tsis5/row.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    rows = file.readlines()

for row in rows:
    s = ""
    if re.findall("[A-Z]", row):
        words = re.split("[A-Z]", row)
        s = " ".join(words)
        print(s)