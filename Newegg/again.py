from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as soup


# target URL
url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card#"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }

response = requests.request("GET", url, headers=headers)
data = soup(response.text, 'html.parser')


# Find all divs with the image tags

image_divs = data.findAll('div', {'class':'item-container'})

# A list to store the image sources
src = []

# Appending each image src while looping through the image divs
for image_container in image_divs:
    
    src.append(image_container.a.img['src'])

print(src)

# Image counter
image_ = 1

# Looping through the image sources
# And writing them to a file
for image in src:
    with open('image_'+ str(image_) + '.jpg', 'wb') as f:
        res = requests.get(image)
        f.write(res.content)
    image_ +=1
