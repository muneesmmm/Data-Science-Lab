c=""
fname=input("Enter file name: ")
f=open(fname,"r")
for line in f:
    i=line.upper()
    c=c+i
print(c)
f.close()
f=open(fname,"w")
f.write(c)
f.close()
