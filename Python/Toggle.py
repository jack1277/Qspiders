text='AbcD@324l'
toggled = ""
for char in text:
    if char.islower():
        toggled += char.upper()
    elif char.isupper():
        toggled += char.lower()
    else:
        toggled += char

print("Toggled string:", toggled)   
