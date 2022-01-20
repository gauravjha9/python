# How to count unique values inside a list

List = [1, 2, 2, 5, 8, 4, 4, 8]
print(List)
# output: 5

# 1st Method
res = []
for i in List:
    if i not in res:
        res.append(i)
print(len(res))

# 2nd Method
# from collections import Counter
# res = Counter(List).keys()
# print(len(res))


# 3rd Method
# res = set(List)
# print(len(res))
