with open("matrix.txt") as f:
    with open("maths.txt","w") as f1:
        for line in f:
            f1.write(line)
fi=open("maths.txt")
li=fi.readlines()
for line in li:
    print(line)
