from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card#'
the_page = urlopen(url)
the_html = the_page.read()

the_page.close() # Closing connection: You have to

# Parsing the HTML
page_soup = soup(the_html, "html.parser")

the_tin = page_soup.findAll('div', {'class':'item-cell'})

the_container = the_tin[0]

the_src = the_container.a.img['src']

print(the_container.a)
