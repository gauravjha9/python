# Remove all duplicates from a given string in Python

txt = 'universe'

dup = []
for i in txt:
    if i not in dup:
        dup.append(i)
print(''.join(dup))