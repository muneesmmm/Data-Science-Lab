#The open() function opens a file, and returns it as a file object.
with open("f1.py") as f:
    with open("f2.py","w") as f1:
        for line in f:
            f1.write(line)
fi=open("f2.py")
li=fi.readlines()
for line in li:
    print(line)
