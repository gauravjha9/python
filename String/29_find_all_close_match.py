# Python | Find all close matches of input string from a list
from difflib import get_close_matches

patterns = ['ape', 'apple', 'peach', 'puppy', 'april']
word = 'appel'


print(get_close_matches(word, patterns))

