# Python – Convert List to List of dictionaries

test_list = ["Mohan", 3, "Ram", 8, 'Raja', 9]
key_list = ["name", "id"]

# output: {'name': 'Mohan', 'id': 3}, {'name': 'Ram', 'id': 8}, {'name': 'Raja', 'id': '9'}]


# 1st Method
res = []
for i in range(0, len(test_list), 2):
    res.append({key_list[0]: test_list[i], key_list[1]: test_list[i+1]})
print(res)


# 2nd Method
# res = [{key_list[0]: test_list[i], key_list[1]: test_list[i+1]} for i in range(0, len(test_list), 2)]
# print(res)