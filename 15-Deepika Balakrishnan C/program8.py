with open("file1.txt") as f:
    with open("file2.txt","w") as f1:
        for line in f:
            f1.write(line)
fi=open("file2.txt")
li=fi.readlines()
for line in li:
    print(line)
