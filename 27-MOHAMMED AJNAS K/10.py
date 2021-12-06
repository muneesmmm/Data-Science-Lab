search_text=input("Enter the word to be replaced : ")
replace_text=input("Enter the new word : ")
abc=input("Enter the name of file with extention : ")
with open(abc,'r') as file:
    data=file.read()
data=data.replace(search_text,replace_text)
with open(abc,'w')as file:
    file.write(data)
print("text replaced")
