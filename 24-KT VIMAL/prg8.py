fname=input("Enter name of the file to copy from: ")
sname=input("Enter name of the file to copy to: ")
with open(fname) as f:
    with open(sname,"w") as f1:
        for line in f:
            f1.write(line)
fi=open(sname)
li=fi.readlines()
for line in li:
    print(line)
