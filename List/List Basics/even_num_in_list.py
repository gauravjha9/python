# Python program to print even numbers in a list

List = [2, 7, 5, 64, 14]
print(List)

# 1st Method
res = []
for i in List:
    if i % 2 == 0:
        res.append(i)
print(res)


# 2nd Method (List Comprehensions)
# res = [i for i in List if not i & 1]
# print(res)


# 3rd Method
# res = list(filter(lambda x: (not x & 1), List))
# print(res)