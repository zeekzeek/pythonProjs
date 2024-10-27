from bs4 import BeautifulSoup
from urllib.request import urlopen

#f = open(r"E:\GitHub\pythonProjs\souperRead\text.txt", "r")
#had to put rawstring for some reason
quote_page = ''
html = urlopen(quote_page).read()
soup = BeautifulSoup(html, 'html.parser')

finder = soup.find_all('a')


for link in finder:
    try:
        if link.get('href').startswith('http') == True:
            print(link.get('href'))
    except AttributeError:
        print('hUh?')

#images = soup.find_all('img')

#for image in images:
#    print(image['src'])
#    print(image['alt'])
#print(finder)
