# Python – Convert Lists of List to Dictionary

test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# output = {('a', 'b'): (1, 2), ('c', 'd'): (3, 4), ('e', 'f'): (5, 6)}

# 1st Method
res = {}
for i in test_list:
    res[tuple(i[:2])] = tuple(i[2:])
print(res)

# 2nd Method
# res = {tuple(i[:2]): tuple(i[2:]) for i in test_list}
# print(res)