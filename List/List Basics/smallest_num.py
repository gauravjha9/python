# Python program to find smallest number in a list

List = [20, 54, 9, -5, 24]

# 1st Method
min = List[0]
for i in range(len(List)):
    if min > List[i]:
        min = List[i]
print(min)


# 2nd Method
# print(min(List))
