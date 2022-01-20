# Python program to find largest number in a list

List = [11, 54, 85, -7, 27]
print(List)

# 1st Method
max = List[0]
for i in range(len(List)):
    if max < List[i]:
        max = List[i]
print(max)


# 2nd Method
# print(max(List))