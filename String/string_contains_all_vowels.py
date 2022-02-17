# Python | Program to accept the strings which contains all vowels

# text = 'Hello world'
text = 'eunoiaai'

vowel = 'aeiou'
s = set({})

for i in text:
    if i in vowel:
        s.add(i)

if len(s) == len(vowel):
    print('Accepted')
else:
    print('Not Accepted')