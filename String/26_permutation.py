# Python | Permutation of a given string using inbuilt function

from itertools import permutations

txt = 'abc'

x = permutations(txt)

for i in x:
    print(''.join(i))