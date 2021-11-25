file=open('eg.txt','r')
count=0
content=file.read()
list=content.split("\n")
for i in list:
    if i:
        count+=1
print("number of lines")
print(count)
