# Python – Pair elements with Rear element in Matrix Row

List = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
print(List)

# Output:- [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]

res = []
for i in List:
    res.append([[j, i[-1]] for j in i[:-1]])
print(res)   