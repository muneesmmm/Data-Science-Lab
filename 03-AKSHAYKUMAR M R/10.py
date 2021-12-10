search_text="hi"
replace_text="hello"
with open(r'sample.txt','r') as file:
    data=file.read()
    data=data.replace(search_text,replace_text)
with open(r'sample.txt','w') as file:
    file.write(data)
print("text replaced")
