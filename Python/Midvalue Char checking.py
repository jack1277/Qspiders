string=input("Enter a string: ")
if len(string) % 2 == 0:
    print("The string does not have a middle character.")
else:
    mid=string[len(string)//2]
    if "A"<= mid <= "Z":
        print("The middle character is an uppercase letter:", mid)