# Python | Count the Number of matching characters in a pair of string

txt1 = 'aabcdef'
txt2 = 'defghia'

# txt1 = 'aabcddekll12@'
# txt2 = 'bb22ll@55k'

a = set(txt1)
b = set(txt2)

# 1st Method
count = 0
for i in a:
    if i in b:
        count += 1
print(count)


# 2nd Method
# match = a & b
# print(len(match))
