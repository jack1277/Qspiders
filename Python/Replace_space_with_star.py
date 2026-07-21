input1=input("Enter a string: ")
while " " in input1:
    input1=input1.replace(" ","*")  
print("String after replacing spaces with '*':",input1)