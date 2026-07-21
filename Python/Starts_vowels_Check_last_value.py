string = input("Enter a string: ")

last_char = string[-1].lower()

if last_char in "aeiou":
    print("The last character is a vowel.")
else:
    print("The last character is not a vowel.")