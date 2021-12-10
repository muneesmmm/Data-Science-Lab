import shutil
f=open("hello.txt")
li=f.readlines()
print (li)
shutil.copyfile("hello.txt","wellcome.txt")
