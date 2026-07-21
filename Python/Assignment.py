"""ch = input("Enter a character: ")

if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
    print("Alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special Character")"""

"""
day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Invalid Day Number")
    """

"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
else:
    print("Invalid Choice")"""

"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is Largest")
elif b > a and b > c:
    print(b, "is Largest")
else:
    print(c, "is Largest")"""

"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b and a > c and a > d:
    print(a, "is Largest")
elif b > a and b > c and b > d:
    print(b, "is Largest")
elif c > a and c > b and c > d:
    print(c, "is Largest")
else:
    print(d, "is Largest")"""

"""temp = int(input("Enter temperature: "))

if temp < 0:
    print("Freezing Weather")
elif temp >= 0 and temp < 10:
    print("Very Cold Weather")
elif temp >= 10 and temp < 20:
    print("Cold Weather")
elif temp >= 20 and temp < 30:
    print("Normal Temperature")
elif temp >= 30 and temp < 40:
    print("It's Hot")
else:
    print("It's Very Hot")"""

ch = input("Enter a character: ")

if ch >= 'a' and ch <= 'z':
    print(ch.upper())
elif ch >= 'A' and ch <= 'Z':
    print(ch.lower())
elif ch >= '0' and ch <= '9':
    print(0)
else:
    print(0)