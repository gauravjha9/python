# Python program to print even length words in a string

text = 'This is a python language'
# text = 'I am Gaurav'

list1 = text.split()

list1 = [i for i in list1 if len(i) % 2 == 0]
print(list1)
