sal=int(input("Enter your salary: "))
high_sal=[]
mid_sal=[]
low_sal=[]
if sal > 50000:
    high_sal.append(sal)
elif sal > 20000 and sal < 50000:
    mid_sal.append(sal)
else:
    low_sal.append(sal)

print("High salary:", high_sal)
print("Mid salary:", mid_sal)
print("Low salary:", low_sal)

