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
# find all with the image tag

one = data.findAll('div', {'class':'item-container'})
src = []
for the_container in one:
    
    src.append(the_container.a.img['src'])



print(src)





# print('Number of Images: ', len(images))
# # for image in images:
# #     print(image)

# # select src tag
# image_src = [x['src'] for x in images]

# for image in image_src:
#     print(image)

image_count = 1
for image in src:
    with open('image_'+str(image_count)+'.jpg', 'wb') as f:
        res = requests.get(image)
        f.write(res.content)
    image_count = image_count+1
