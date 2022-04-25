
import requests
from bs4 import BeautifulSoup as soup

import pandas as pd

url = 'https://www.newegg.com/p/pl?d=recording+microphones'

html_data = requests.get(url) # Send a GET request to the url

# Make a BS4 obj out of the contents of the respone
soup_data = soup(html_data.content, 'html.parser') 
print('Status: ', html_data.status_code)
print(type(html_data))
print(type(soup_data))

# Get the item cells
items = soup_data.find(class_='item-cells-wrap')

print('Item-cells: ', len(items))

# Get all the microphones
mics = items.find_all(class_='item-container')
# print(mics.prettify())

descriptions = []
prices = []

for mic in mics:    
    description = mic.find(class_='item-info')
    desc = description.find(class_='item-title').get_text()
    descriptions.append(desc)

    mic_price = mic.find(class_='item-action')
    price = mic_price.find(class_='price-current').strong.get_text()
    prices.append(price)


data = pd.DataFrame({
    'Description' : descriptions,
    'Price' : prices
})

print(data)



