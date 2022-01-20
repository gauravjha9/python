# Python | Program to print duplicates from a list of integers

List = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(List)

# 1st Method
res = []
for i in range(len(List)):
    for j in range(i+1, len(List)):
        if List[i] == List[j] and List[i] not in res:
            res.append(List[j])
print(res)


# 2nd Method
# from collections import Counter
# d = Counter(List)
# print(d)

# res = [item for item in d if d[item]>1]
# print(res)