# Python | Sum of number digits in List

List = [12, 67, 98, 34]
print(List)

# 1st Method
List2 = []
for ele in List:
    s = 0
    for l in str(ele):
        s += int(l)
    List2.append(s)
print(List2)


# 2nd Method
# res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), List))
# print(res)
