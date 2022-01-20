# Python program to select Random value form list of lists

List = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

from itertools import chain
import random

res = random.choice(list(chain.from_iterable(List)))
print(res)