import os
path = 'C:\\Users\\zhang\\Desktop\\pp2\\pp2\\tsis6\\exz\salam.txt'
path_bool = os.access(path, os.F_OK)

if path_bool == False:
    print("NO")
elif path_bool == True:
    os.remove(path)
    print("YES")