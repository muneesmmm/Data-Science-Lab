search_text="Universe"
replace_text="World"
with open(r'pg10.txt','r') as file:
    data=file.read()
    data=data.replace(search_text,replace_text)
with open(r'pg10.txt','w') as file:
    file.write(data)
print("text replaced")
