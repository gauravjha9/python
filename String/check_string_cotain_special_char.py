# Program to check if a string contains any special character

txt = input('Enter the text: ')
sp_ch = '[@_!#$%^&*()<>?/\|}{~:]'

for i in txt:
    if i in sp_ch:
        print('Not accepted')
        break
else:
    print('accepted')

# 2nd Method

# import re
# r = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

# if (r.search(txt) == None):
#     print('Accepted')
# else:
#     print('Not accepted')


      
    