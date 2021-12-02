fname=input("Enter file name: ")
with open(fname,'r') as file:
    counter=0
    content=file.read()
    colist=content.split("\n")
    for i in colist:
        if i:
            counter+=1
print("No of lines in the file:",counter)
