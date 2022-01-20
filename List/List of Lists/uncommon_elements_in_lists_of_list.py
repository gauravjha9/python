# Python | Uncommon elements in Lists of List

list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [[3, 4], [5, 7], [1, 2]]

# 1st Method
l1 = set(map(tuple, list1))
l2 = set(map(tuple, list2))
res = l1 ^ l2
print(list(res))