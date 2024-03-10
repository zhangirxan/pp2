import os
path = r"C:\Users\zhang\Desktop\pp2\pp2\tsis6\exz"

if os.path.exists(path):
    print("path exists")
else:
    print("path does not exist")
if os.access(path, os.R_OK):
    print("readability")
else:
    print("not readability")
if os.access(path, os.W_OK):
    print("writabillity")
else:
    print("not writabillity")
if os.access(path, os.X_OK):
    print("executability")
else:
    print("not executability")