# Python program to print all even numbers in a range

start = 4
end = 15

# 1st Method
res = []
for i in range(start, end+1):
    if not i&1:
        res.append(i)
print(res)


# 2nd Method
# res = [i for i in range(start, end+1) if not i & 1]
# print(res)


# 3rd Method
# res = list(filter(lambda x: not x & 1, range(start, end+1)))
# print(res)