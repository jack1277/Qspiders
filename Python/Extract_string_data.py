l=[1,2.3,True,'Python','c','c++','java',3+2j]
a=[]
for i in l:
    if type(i)==str:
        a.append(i)
print(a)