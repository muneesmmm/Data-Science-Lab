a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=input("Enter number"+str(i)+":")
    a.append(b)
nodupe=list(dict.fromkeys(a))
print(nodupe)