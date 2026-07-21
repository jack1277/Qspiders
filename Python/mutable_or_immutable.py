data1=eval(input("Enter a data: "))
if type(data1) in (list,dict,set):
    print("Mutable data type")
else:
    print("Immutable data type")