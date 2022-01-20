# Python program to print negative numbers in a list

List = [12, -7, 5, 64, -14]
print(List)

# 1st Method
res = []
for i in List:
    if i < 0:
        res.append(i)
print ('Negative Numbers in list: ',res)


# 2nd Method
# res = [i for i in List if i < 0]
# print ('Negative Numbers in list: ',res)


# 3rd Method
# res = list(filter(lambda x: x < 0, List))
# print ('Negative Numbers in list: ',res)
