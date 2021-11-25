search_text="hai"
replace_text="hello"
with open(r'abc.txt','r') as file:
	data=file.read()
data=data.replace(search_text,replace_text)
with open(r'abc.txt','w') as file:
    file.write(data)
print("text replaced")


