a=[2143,136,2]
b=a[0]
for i in a:
    if type(b)!=type(i):
        print("Hetero")
        break
else:
    print("Homo")