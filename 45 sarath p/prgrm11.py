file = open("prgrm11.py","r")
counter = 0
content = file.read()
colist = content.split("\n")
for i in colist:
    if i:
        counter += 1
print("This is the number of lines in the file")
print (counter)
        
