with open("f.txt") as a:
    with open("f1.txt","w") as b:
        for line in a:
            b.write(line)
fi=open("f1.txt")
li=fi.readlines()
for line in li:
    print(line)
