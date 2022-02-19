with open("pg8-1.txt") as f:
    with open("pg8-2.txt","w") as f1:
        for line in f:
            f1.write(line)
fi=open("file2.txt")
li=fi.readlines()
for line in li:
    print(line)
