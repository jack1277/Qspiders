l=[1,1,2,1,3,3,4,2,4,5,6]
output=[]
for i in l:
    if i not in output:
        output.append(i)
print(output)
