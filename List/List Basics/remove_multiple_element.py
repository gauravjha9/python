# Remove multiple elements from a list in Python

List = [12, 15, 3, 10]
print(List)
remove_ele = [12, 3]

# 1st Method
for i in remove_ele:
    List.remove(i)
print(List)


# 2nd Method
# List = [i for i in List if i not in remove_ele]
# print(List)


# 3rd Method (Remove by Position)
# remove_pos = [0, 2]

# for i in sorted(remove_pos):
#     del List[i]
# print(List)