import os
path = r"C:\Users\zhang\Desktop\pp2\pp2\tsis6\exz"

print("Directories:")
for entry in os.scandir(path):
    if entry.is_dir():
        print(entry.name)

print("\nFiles:")
for entry in os.scandir(path):
    if entry.is_file():
        print(entry.name)

print("\nAll Directories and Files:")
for entry in os.scandir(path):
    print(entry.name)