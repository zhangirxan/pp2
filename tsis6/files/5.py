import os

mylist = ['a','b','c','d','e']

with open('C:\\Users\\zhang\\Desktop\\pp2\\pp2\\tsis6\\exz\written_text.txt' , 'w') as file:
    for i in mylist:
        file.write(i + '\n')
file.close()