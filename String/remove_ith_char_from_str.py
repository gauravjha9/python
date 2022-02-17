# Python program for removing i-th character from a string

txt = 'python'
pos = 2

new_txt = txt[:pos-1] + txt[pos:]
print(new_txt)        