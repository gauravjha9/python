# Python – Remove empty List from List

List = [5, 6, [], 3, [], [], 9]
print(List)

# 1st Method
List = [i for i in List if i]
print(List)