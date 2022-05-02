# Python – Uppercase Half String

text = 'apples'

half = len(text)//2

res = text[:half] + text[half:].upper()
print(res)
