#get current date and time onto clipboard from desktop

import time, sys, pyperclip

obj = time.asctime()
sys.argv

pyperclip.copy(obj)
print(obj)

