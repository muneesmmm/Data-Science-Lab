file=open("abc.txt","r")
counter=0
content=file.read()
colist=content.split("\n")
for i in colist:
    if i:
        counter+=1
        print("this is the no: of lines in the file")
        print(counter)
