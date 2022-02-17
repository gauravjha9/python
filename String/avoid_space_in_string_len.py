# Python – Avoid Spaces in string length

text = 'Hello world'

# 1st Method
count = 0
for i in text:
    if i != ' ':
        count+=1
print(count)


# 2nd Method
# res = sum(not i.isspace() for i in text)
# print(res)