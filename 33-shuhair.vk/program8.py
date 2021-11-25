with open("sample.txt") as f:
    with open("cd.txt","w") as f1:
        for line in f:
            f1.write(line)
fi=open("cd.txt")
li=fi.readlines()
for line in li:
    print(line)
