import re

message = 'call me at 83233707 tomorrow hor'

phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d') #use backslash not forward slash
mo = phoneNumRegex.search(message)
print(mo.group())
