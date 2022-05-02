# Python | Check for URL in a String

import re

r = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

s = 'My Profile: https://auth.geeksforgeeks.org/user/ram%20nka/articles in the portal of https://www.geeksforgeeks.org/'

url = re.findall(r, s)

result = [i[0] for i in url]
print(result)