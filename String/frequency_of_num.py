# Python | Frequency of numbers in String

txt = 'geeks4feeks is No. 1 4 geeks'

count = 0
for i in txt:
    if i.isnumeric():
        count += 1
print(count)