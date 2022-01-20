# Python program to find second largest number in a list

# List = [10, 20, 4]
# List = [10, 20, 4, 45, 99]
List = [70, 11, 100, 20, 4, 100]

# 1st Method
res = sorted(set(List))
print(res[-2])


# 2nd Method
# max = List[0]
# secMax = max

# for i in range(len(List)):
#     if max < List[i]:
#         secMax = max
#         max = List[i]
# print(secMax)