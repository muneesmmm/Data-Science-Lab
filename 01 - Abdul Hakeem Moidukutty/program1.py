temp=int(input("Enter number of elements"))
numlist=[]
for i in range (1,temp+1):
    num=int(input("Enter number " + str(i) + ":"))
    numlist.append(num)
print("The largest number is " + str( max(numlist)) )
