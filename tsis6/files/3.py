import os
path = r"C:\\Users\\zhang\\Desktop\\pp2\\pp2\\tsis6\abc.txt"

if os.path.exists(path):
    print("Directories:")
    for entry in os.scandir(path):
        if entry.is_dir():
            print(entry.name)

    print("\nFiles:")
    for entry in os.scandir(path):
        if entry.is_file():
            print(entry.name)
