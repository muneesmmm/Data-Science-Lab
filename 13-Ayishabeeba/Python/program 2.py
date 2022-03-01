list1=[1,2,3,4,4]
print(list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)        
