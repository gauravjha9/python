# Python program to find uncommon words from two Strings

a = "Geeks for Geeks"
b = "Learning from Geeks for Geeks"

l = a.split()
l2 = b.split()

# 1st method
result = []
for i in l:
    if i not in l2:
        result.append(i)
for j in l2:
    if j not in l:
        result.append(j)
print(result)


# 2nd method
# print(set(l) ^ set(l2))
