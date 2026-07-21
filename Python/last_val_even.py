num=int(input("Enter a number: "))
while num>0:
    last_digit = num % 10
    if last_digit % 2 == 0:
        print("The last digit is even.")
    else:
        print("The last digit is odd.")
    break
