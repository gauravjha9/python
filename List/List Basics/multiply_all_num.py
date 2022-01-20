# Python | Multiply all numbers in the list

from functools import reduce
List = [3, 4, 8]
print(List)

# 1st Method
p=1
for ele in List:
    p *= ele
print('Multiplication of All numbers in List: ', p)

# 2nd Method
# res = reduce((lambda x, y: x * y), List)
# print('Multiplication of All numbers in List: ', res)


# 3rd Method
# import numpy
# print(numpy.prod(List))


# 4th Method
# import math
# print(math.prod(List))
