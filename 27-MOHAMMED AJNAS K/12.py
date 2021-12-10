c=0
abc=input("Enter the name of file with extention : ")
with open(abc,'r') as file:
    data=file.read()
lines=data.split("\n")
for i in lines:
    if "11" in i:
        print(i)
