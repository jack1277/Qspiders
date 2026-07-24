"""

 for i in range(2,10,2):
    if i==4 or i == 6:
        break
    print(i)

    """
"""
for i in range(2,10):
    if i==3 or i==5:
        print(i)
    break

"""
"""
for i in range(1,10):
    print(i)
    break
"""
"""
for i in range(1,10):
    break
    print(i) 
"""
"""
for i in range(1,10,2):
    if i==3 and i==5:
        break
    print(i)
    
"""
"""
for i in range(2,10,2):
    if i==3 or i==2:
        print(i)
    break
"""
"""
for i in range(2,5):
    if i>3:
        print(i)
    break
print(i)
"""
l=['a','b','c','d',4,3.4,8.3,2+3j,[1,2,3]]
for i in l:
    if type(i)!=str:
        break
    print(i)
