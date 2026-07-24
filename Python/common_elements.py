l1=[3,2,5,7,9,11]
l2=[5,15,11,13,4,7,2]
common=[]
for i in l1:
    if i in l2:
        common.append(i)

print(common)