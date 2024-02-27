import re
file_path = r"C:\Users\zhang\Desktop\pp2\pp2\tsis5\row.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    rows = file.readlines()

for row in rows:
    s = ""
    if re.findall("_", row):
        words = row.split("_")
        for i in range(len(words)):
            words[i] = words[i].title()
        s = "".join(words)
        print(s)