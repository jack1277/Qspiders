list1 = [10, 20, 30, 40, 50, 60, 70]

if len(list1) > 10:
    list1[-1] = list1[0]
    print(list1)
else:
    print(str(list1[0])[::-1])
    print(str(list1[-1])[::-1])