from bs4 import BeautifulSoup
from urllib.request import urlopen

#f = open(r"E:\GitHub\pythonProjs\souperRead\text.txt", "r")
#had to put rawstring for some reason
quote_page = 'https://www.reddit.com/r/SquaredCircle/comments/1fmaos2/fightful_wwe_sources_claim_to_fightfulselect_that/'
html = urlopen(quote_page).read()
soup = BeautifulSoup(html, 'html.parser')

#finder = soup.find_all('a')

#for link in finder:
#    print(link.get('href'))

images = soup.find_all('img')

for image in images:
    print(image['src'])
#    print(image['alt'])
#print(finder)
