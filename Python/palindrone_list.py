a = eval(input("Enter a list: "))
reversed_list = a[::-1]

if reversed_list == a:
    print(f"{a[0]} and {a[-1]}")
else:
    print(a[1:len(a) - 1])
