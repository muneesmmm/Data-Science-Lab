
# Python program to count the 
# number of lines in a text file
  
  
# Opening a file
file = open("Samplefile.txt","r")
Counter = 0
  
# Reading from file
Content = file.read()
CoList = Content.split("\n")
j=input("Enter the word from a line")  
for j in CoList:
    for i in CoList:
        print(i)
        
