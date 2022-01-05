#program to capitalise each word in a file
file_gfg=open('1.txt','r')
for line in file_gfg:
    output=line.upper()
print(output)
