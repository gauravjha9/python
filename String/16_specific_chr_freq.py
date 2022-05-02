# Python – Specific Characters Frequency in String List

from collections import Counter

txt = ["geeksforgeeks is best for geeks"]
ch_list = ['e', 'b', 'g', 'f']


res = {key:val for key, val in dict(Counter("".join(txt))).items() if key in ch_list}
print(res)