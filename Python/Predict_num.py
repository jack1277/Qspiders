import random
num=random.randint(1,20)
entries = 5
i=1
while i<=entries:
    choice = int(input("Enter your num"))
    if num == choice:
        print("Num is matched")
        break
    elif num>choice:
        print("Enter Larger number")
    elif num<choice:
        print("Enter Lower number")
    i=i+1