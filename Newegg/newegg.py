from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card#'

# Opening connection to the website and grabbing the page
the_page = urlopen(url)
the_html = the_page.read()

the_page.close() # Closing connection: You have to

# Parsing the HTML
page_soup = soup(the_html, "html.parser")

# Grabs each card
card_containers = page_soup.findAll("div", {"class":"item-container"})

# print(card_containers)

# First Card
card_one = card_containers[0]

# The first image
card_one_img = card_containers[0].a.img

# The image src
image_src = card_one.img['src']

# print(image_src)

# Create a CSV file to store the data we collect
filename = "products.csv"

# Open it for writing
f = open(filename, 'w')

# Column names
headers = "Brand, Product_name, Shipping\n" # New Lines for csv.

f.write(headers) # The first line to write are the headers..

# Looping through the divs with the cards

for container in card_containers:

    # image = container.div.img
    brand = container.div.a.img['title']
    
    title_container = container.findAll('a', {'class':'item-title'})

    product_name = title_container[0].text

    shipping_container = container.findAll('li', {'class': 'price-ship'})

    shipping = shipping_container[0].text

    print("The Brand: ", brand)
    print("Product Name: ", product_name)
    print("Shipping: ", shipping)

    # Every time the loop runs, the file is written

    f.write(brand + ',' + product_name.replace(',', '|') + ',' + shipping + "\n")

# You have to close the file
# Otherwise you can't open it later
f.close()

