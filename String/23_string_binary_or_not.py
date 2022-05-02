# Python | Check if a given string is binary string or not

txt = '1010110101'
print(txt)

is_bin = False

if txt.isdigit():
    l = ' '.join(txt).split()
    for i in l:
        if int(i) == 0 or int(i) == 1:
            is_bin = True
        else:
            is_bin = False
            break
if is_bin == True:
    print('Yes, It is Binary')
else:    
    print('No, It is not Binary')
