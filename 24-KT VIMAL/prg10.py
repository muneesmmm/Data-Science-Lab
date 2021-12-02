fname=input("Enter file name: ")
search_text=input("Enter text to search: ")
replace_text=input("Enter text to replace: ")
with open(fname,'r') as file:
	data=file.read()
data=data.replace(search_text,replace_text)
with open(fname,'w') as file:
    file.write(data)
print("text replaced")
