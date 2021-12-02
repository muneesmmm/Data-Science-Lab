
with open("file.txt") as f:
    with open("ss.txt","w") as f1:
        for line in f:
            f1.write(line)
fi=open("ss.txt")
li=fi.readlines()
for line in li:
    print(line)
