search_text = "Hello"
replace_text = "Hii"
with open('ab.txt', 'r') as file:
    data = file.read()
    print("Old Content : ",data)
    data = data.replace(search_text, replace_text)
with open('ab.txt', 'w') as file:
    file.write(data)
print("New Content : ",data)
