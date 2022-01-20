# Python | Ways to check if element exists in list

List = [4, 5, 2, 9, 6, 7]
find_ele= 8

# 1st Method
# for i in range(len(List)):
#     if i == find_ele:
#         print(f'{i} is Exist in the List')
#         break
# else:
#     print(f'{i} is not Exist in the List')


# 2nd Method
if find_ele in List:
    print(f'{find_ele} is Exist in the List')
else:
    print(f'{find_ele} is not Exist in the List')
    