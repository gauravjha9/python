# Reverse words in a given String in Python

text = 'Hello world in Pyton'

list1 = text.split()
list2 = list1[::-1]

res = ' '.join(list2)
print(res)