number=int(input("Enter a number: "))
if number % 2 == 0 and number % 5 == 0:
    print(f"{number} is even and divisible by 5.")
else:
    print(f"{number} is not even and divisible by 5.")