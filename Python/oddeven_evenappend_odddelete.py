list1 = input("Enter a list: ")
list1 = list1.split(",")

if len(list1) % 2 == 0:
    list1.append("0")
    print("List after appending 0:", list1)
else:
    list1.pop()
    print("List after deleting last element:", list1)