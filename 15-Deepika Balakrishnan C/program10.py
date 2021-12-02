search_text = "HELLO"
replace_text = "HII"
with open('file1.txt', 'r') as file:
    data = file.read()
    print("Old Content : ",data)
    data = data.replace(search_text, replace_text)
with open('file1.txt', 'w') as file:
    file.write(data)
print("New Content : ",data)
