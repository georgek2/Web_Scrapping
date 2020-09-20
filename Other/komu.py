from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card#'
the_page = urlopen(url)
the_html = the_page.read()

# Closing connection after reading the page
the_page.close() 

# Parsing the HTML
page_html = soup(the_html, "html.parser")

item_cells = page_html.findAll('div', {'class':'item-cell'})

# The first item cell
the_container = item_cells[0]

# Printing the a tag 
print(the_container.a)

# The image source
the_src = the_container.a.img['src']

print(the_src)
