# Python program to check if a string has at least one letter and one number

text = 'hello2 world'

l = False
n = False
for i in text:
    if i.isalpha():
        l = True
    if i.isdigit():
        n = True

print(l and n)
    