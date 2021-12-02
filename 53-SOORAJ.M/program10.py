search_text="wow"
replace_text="yeah"
with open(r'new.txt','r') as file:
    data=file.read()
    data=data.replace(search_text,replace_text)
with open(r'new.txt','w') as file:
    file.write(data)
print("text replaced")
