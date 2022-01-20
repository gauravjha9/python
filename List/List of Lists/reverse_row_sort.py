# Python – Reverse Row sort in Lists of List

List = [[4, 1, 6], [7, 8], [4, 10, 8]]
print(List)

# 1st Method
for i in List:
    i.sort(reverse=True)
print(List)


# 2nd Method
# List = [sorted(i, reverse=True) for i in List]
# print(List)
