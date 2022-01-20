# Python program to print all negative numbers in a range

start = -4
end = 9

# 1st Method
res = []
for i in range(start, end+1):
    if i < 0:
        res.append(i)
print(res)


# 2nd Method
# res = [i for i in range(start, end+1) if i < 0]
# print(res)


# 3rd Method
# res = list(filter(lambda x: x < 0, range(start, end+1)))
# print(res)