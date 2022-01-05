a=[]
n = int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int( input("Enter number:"+str(i)+":"))
    a.append(b)
print("Largest element is:" + str( max(a)))