# Python – Test if List contains elements in Range

List = [4, 5, 7, 9]
# range
s, e = 3, 10

# 1st Method
res = True
for i in List:
    if i < s or i >= e:
        res = False
        break
print(res)



# 2nd Method
# res = all(i > s and i <= e for i in List)
# print(res)
