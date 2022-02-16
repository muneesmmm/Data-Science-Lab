def common_num(a,b):
     result = False
     for i in a:
         for j in b:
             if i == j:
                 result = True
                 return result
     return result           


list1 = []
n = int(input("Enter number of elements list1:"))
for i in range(1,n+1):
    e1=int( input("Enter element:"))
    list1.append(e1)

list2 = []
m = int(input("Enter number of elements list2:"))
for i in range(1,m+1):
    e2=int( input("Enter element:"))
    list2.append(e2)
print(common_num(list1,list2))

