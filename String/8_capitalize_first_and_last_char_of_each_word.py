# Python program to capitalize the first and last character of each word in a string

text = 'hello world' 
text = 'welcome to the earth' 


# 1st Method
list1 = text.split()
list2 = []
for i in list1:
    t = i[:-1].title() + i[-1].upper()
    list2.append(t)
res = ' '.join(list2)
print(res)
