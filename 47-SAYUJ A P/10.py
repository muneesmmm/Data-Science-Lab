search_text="hello"
replace_text="guys"
with open(r'sample.txt','r') as file:
    data=file.read()
    data=data.replace(search_text,replace_text)
with open(r'sample.txt','w') as file:
    file.write(data)
print("text replaced")
