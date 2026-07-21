a=eval(input("Enter a list of elements: "))
if len(a) % 2 == 1:
    mid = a[len(a)//2]
    if type(mid) == int:
        print("The middle element is an integer:", mid)
    else:
        print("The middle element is not an integer:", mid)
else:
    print("The list does not have a middle Value.")