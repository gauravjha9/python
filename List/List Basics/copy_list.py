# Python | Cloning or Copying a list

List = [3, 4, 5, 6, 7, 9]
print(List)


# 1st Method
List2 = List.copy()
print('Copied List: ',List2)
print(id(List), id(List2))


# 2nd Method
# List3 = List[:]
# print('Copied List: ', List3)
# print(id(List), id(List3))


# 3rd Method
# List4 = []
# for i in List:
#     List4.append(i)
# print('Copied List: ',List4)
# print(id(List), id(List4))