# Python program to count positive and negative numbers in a list

List = [2, -7, 5, -64, -14]
print(List)

# 1st Method
posCount = negCount = 0
for i in List:
    if i >= 0:
        posCount += 1
    else:
        negCount += 1
print('Positive Numbers in List: ', posCount)
print('Negative Number in List: ', negCount)  


# 2nd Method
# posCount = [i for i in List if i >= 0]
# print('Positive Numbers in List: ', len(posCount))
# negCount = [i for i in List if i < 0]
# print('Negative Number in List: ', len(negCount))  


# 3rd Method
# posCount = list(filter(lambda x: x >= 0, List))
# print('Positive Numbers in List: ', len(posCount))
# negCount = len(List) - len(posCount)
# print('Negative Number in List: ', negCount)  

