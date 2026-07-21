text = input("Enter a string: ")
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text = reversed_text + text[i]

if reversed_text == text and len(text) >= 10:
    print("The string is a palindrome and its length is greater than or equal to 10:", text)
elif reversed_text == text and len(text) < 10:
    print("The string is a palindrome and its length is less than 10:", text)
else:
    print("The string is not a palindrome:", text)
