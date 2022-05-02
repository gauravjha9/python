# Python program to check whether the string is Symmetrical or Palindrome

text = 'khokho'
# text = 'nitin'
# text = 'amaama'

len = len(text)
half_len = len//2

if text[:half_len] == text[half_len:]:
    print('Symetrical')
else:
    print('Not Symetrical')

if text == text[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')