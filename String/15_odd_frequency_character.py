# Python – Odd Frequency Characters

from collections import Counter


txt = 'geekforgeeks is best for geeks'
print(f'The original string: {txt}')


res = [chr for chr, count in Counter(txt).items() if  count & 1]
print(res)





