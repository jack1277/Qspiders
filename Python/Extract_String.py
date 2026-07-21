s="SharAn32@gmail.com"
upper=""
lower=""
digits=""
special=""
i=0
while i<len(s):
    if 'A'<=s[i]<='Z':
        upper+=s[i]
    elif 'a'<=s[i]<='z':
        lower+=s[i]
    elif '0'<=s[i]<='9':
        digits+=s[i]
    else:
        special+=s[i]
    i+=1

print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")
print(f"Digits: {digits}")
print(f"Special characters: {special}")