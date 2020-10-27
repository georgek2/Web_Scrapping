import requests
from bs4 import BeautifulSoup as soup 

resp = requests.get('https://www.newegg.com/p/pl?d=monitors+with+webcam+and+speakers')

# print(resp.status_code)

page = soup(resp.content, 'html.parser')

item_containers = page.find_all(class_='item-container')

# print(item_containers[0].prettify())

f = 'monitors.csv'

f = open('monitors.csv', 'w')

headers = "Brand, Description, Price, src\n"

# for item in item_containers:
#     descs = item.select('.item-info .item-title')
    
m_one = item_containers[8]
# brand = m_one.div.div.a.img['alt']
src = m_one.img['src']
desc = m_one.img['title']

price = m_one.find(class_='price-current').strong.get_text()

print(m_one)

f.write(headers)
for container in item_containers:
    brand = container.div.div.a.img['alt']
    desc = container.img['title']
    price = container.find(class_='price-current').strong.get_text()
    src = container.img['src']

    print('The brand : ', brand)
    print('DEscription : ', desc)
    print('Price: ', price)

    f.write(brand + ',' + desc.replace(',', '|') + ',' + ',' + price + ',' + src + '\n')

f.close()