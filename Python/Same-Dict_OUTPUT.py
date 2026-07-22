d = {'a': 'a', 2: 2, 4: 5, 9: 3.5, 'apple': 'apple'}
new = {}
for key, value in d.items():
    if key == value:
        new[key] = value
print(new)