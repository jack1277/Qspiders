num=int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("HiHello")
elif num % 3 == 0:
    print("Hi")
elif num % 7 == 0:
    print("Hello")
else:
    print("The number is not divisible by 3 or 7.")