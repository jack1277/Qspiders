groom_age = int(input("Enter Groom Age: "))
bride_age = int(input("Enter Bride Age: "))

if groom_age >= 21 and bride_age >= 18:
    print("Eligible for Marriage")
else:
    print("Not Eligible for Marriage")