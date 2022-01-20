# Python – Extract elements with Frequency greater than K

List = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

res = []
for i in List:
    freq = List.count(i)
    
    if freq > k and i not in res:
        res.append(i)
print(res)