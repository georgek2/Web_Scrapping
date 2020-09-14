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

card_one = card_containers[0].a.img['src']

image = urlopen(card_one)

print(image)


# print(card_one)
# image = card_one.div.a.img

# Throwing the results into a CSV file

# filename = "products.csv"
# f = open(filename, 'w')

# headers = "Brand, Product_name, Shipping\n" # New Lines for csv.

# f.write(headers) # The first line to write are the headers..

# for container in card_containers:

#     image = container.div.img
#     brand = container.div.a.img['title']
    
#     title_container = container.findAll('a', {'class':'item-title'})

#     product_name = title_container[0].text

#     shipping_container = container.findAll('li', {'class': 'price-ship'})

#     shipping = shipping_container[0].text

#     print("The Brand: ", brand)
#     print("Product Name: ", product_name)
#     print("Shipping: ", shipping)

#     # Every time the loop runs, the file is written

#     f.write(brand + ',' + product_name.replace(',', '|') + ',' + shipping + "\n")

# # You have to close the file
# # Otherwise you can't open it later
# f.close()

