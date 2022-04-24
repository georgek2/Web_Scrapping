from matplotlib.pyplot import cla
import requests
from bs4 import BeautifulSoup as soup

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
mics = items.find(class_='item-container')
# print(mics.prettify())
descriptions = mics.find_all(class_='item-branding')
print(len(descriptions))
mic_prices = mics.find_all('item-action')
print(len(mic_prices))





