# Python program to count number of vowels using sets in given string

txt = 'Hello world'
vowel = 'aeiouAEIOU'

count = 0
for i in txt:
    if i in vowel:
        count += 1
print(count)