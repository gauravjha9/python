# Find words which are greater than given length k

txt = 'hello geeks for geeks is Computer science portal'

k = int(input('Enter the length: '))
# k = 4

l = txt.split()
new_list = []
for i in l:
    if len(i) > k:
        new_list.append(i)
    
print(new_list)