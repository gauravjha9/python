# Python – List product excluding duplicates

List = [1, 3, 5, 6, 3, 5, 6, 1]

# 1st Method
List2 = []
prod = 1
for i in List:
    if i not in List2:
        List2.append(i)
        prod *= i        
print(prod)



# 2nd Method
# import functools

# prod = functools.reduce(lambda x,y: x*y, set(List), 1)
# print(prod)