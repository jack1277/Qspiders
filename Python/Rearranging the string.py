first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

if first_name[0] == last_name[-1]:
    print(first_name[::-1])
    print(last_name[::-1])
else:
    print(first_name)
    print(last_name)