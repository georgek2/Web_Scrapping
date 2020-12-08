import requests
from bs4 import BeautifulSoup as soup 

import pandas as pd

response = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324')

print(response.status_code)

page_content = soup(response.content, 'html.parser')

# print(page_content)

tombstones = page_content.findAll(class_='forecast-tombstone')

first = tombstones[0]

# print(first)

f = open('again.csv', 'x')

headers = "Period_Tag, Short_Desc, Long_Desc\n"

f.write(headers)

for tombstone in tombstones:

    periods = tombstone.select('.tombstone-container .period-name')
    for period_name in periods:
        Period_Tag = period_name.get_text()
    
    short_desc = tombstone.find(class_='short-desc').get_text()
    long_desc = tombstone.img['alt']
    
    f.write(Period_Tag + ',' + short_desc.replace(',', '|') + ',' + long_desc.replace(',', '|') + '\n')

f.close()

df = pd.read_csv('again.csv')
# print(df)

info = {
    'p_tags': [],
    'short_desc': [],
    'long_desc': []
}

for tombstone in tombstones:
    
    periods = tombstone.select('.tombstone-container .period-name')
    for period_name in periods:
        Period_Tag = period_name.get_text()
        info['p_tags'].append(Period_Tag)

    short_desc = tombstone.find(class_='short-desc').get_text()
    long_desc = tombstone.img['alt']
    
    info['short_desc'].append(short_desc)
    info['long_desc'].append(long_desc)

df = pd.DataFrame(info)

print(df)