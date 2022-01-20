# Python program to count Even and Odd numbers in a List

List = [2, 7, 5, 64, 14]
print(List)


# 1st Method
# evenCount = 0
# oddCount = 0
# for i in List:
#     if not i & 1:
#         evenCount += 1
#     else:
#         oddCount += 1
# print('Even number in list: ', evenCount)
# print('Odd number in list: ', oddCount)


# 2nd Method
# evenCount = [i for i in List if not i & 1]
# print('Even number in list: ', len(evenCount))

# oddCount = [i for i in List if i & 1]
# print('Odd number in list: ',len(oddCount))


# 3rd Method
# evenCount = [i for i in List if not i & 1]
# print('Even number in list: ', len(evenCount))
# oddCount = len(List) - len(evenCount)
# print('Odd number in list: ',oddCount)
