from bs4 import BeautifulSoup
from urllib.request import urlopen

#f = open(r"E:\GitHub\pythonProjs\souperRead\text.txt", "r")
#had to put rawstring for some reason
quote_page = 'https://www.erome.com/a/Yl4YnSaS'
html = urlopen(quote_page).read()
soup = BeautifulSoup(html, 'html.parser')

finder = soup.find_all('a')


for link in finder:
    try:
        if link.get('img').startswith('http') == True:
            print(link.get('img'))
    except AttributeError:
        print('hUh?')

#images = soup.find_all('img')

#for image in images:
#    print(image['src'])
#    print(image['alt'])
#print(finder)
