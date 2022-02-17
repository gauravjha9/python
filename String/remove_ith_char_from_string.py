# Ways to remove i'th character from string in Python

text = 'Hello world'
pos = 3


# 1st Method
new_text = ''
for i in range(len(text)):
    if i != pos:
        new_text += text[i]
print(new_text)


# 2nd Method
# new_text = text[:pos-1] + text[pos:]
# print(new_text)