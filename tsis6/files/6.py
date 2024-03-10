import string

for char in string.ascii_uppercase:
    file = open('C:\\Users\\zhang\\Desktop\\pp2\\pp2\\tsis6\\exz\{fchar}'.format(fchar = char), 'x')
    file.close()