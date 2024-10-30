from bs4 import BeautifulSoup

soup = BeautifulSoup("https://curator-test.bandlab.com/sounds/collections/samples/214a93f1-b23f-41e5-bd40-f6fc97dc408b", "html.parser")
mydivs = soup.finda_all
