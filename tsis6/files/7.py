with open("C:\\Users\\zhang\\Desktop\\pp2\\pp2\\tsis6\\exz\abc.txt") as file1, open("C:\\Users\\zhang\\Desktop\\pp2\\pp2\\tsis6\\exz\text.txt") as file2:
    for line in file1:
        file2.write(line)