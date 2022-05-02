# Python | Swap commas and dots in a String

a = '232,128,33,5439'
print(a)


l = list(a)
for i in range(len(l)):
    if l[i] == ',':
        l[i] = '.'
r = ''.join(l)
print(r)
