#run mapit from desktop
#copy from clipboard
#execute content on google maps

import webbrowser, sys, pyperclip
#webbrowser and sys argument for pasting value after mapit

sys.argv # ['mapit.py', '662', 'Bedok']

# check if command line arguments were passed

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/search/' + address)
