import re
import functools

file_path=r"C:\Users\zhang\Desktop\pp2\pp2\tsis6\files\aa.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    rows = file.readlines()

for row in rows:
    if re.search("[0-9]", row):
        nums = re.findall("[0-9]*", row)
        modified_row = "," .join(nums)
        print("[",modified_row,"]")

