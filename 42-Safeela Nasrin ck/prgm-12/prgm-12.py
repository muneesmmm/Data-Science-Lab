import re
count=0
def string_match(text):
    pattern='^11'
    if re.search(pattern,text):
        global count
        count=count+1
bitfile = open('bitfile12.txt','r')
while True:
    data = bitfile.readline()
    if not data:
        break
    else:
        string_match(data)
print (count)
bitfile.close()
