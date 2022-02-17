# Python – Least Frequent Character in String

txt = 'geeksforgeeks'
print('The original string: ', txt)


# 1st method
freq = {}
for i in txt:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
print(min(freq, key=freq.get))


# 2nd Method
# from collections import Counter

# res = Counter(txt)
# res = min(res, key = res.get)

# print(res)