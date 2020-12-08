import requests
from bs4 import BeautifulSoup as soup 
import pandas as pd 

resp = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324')

page = soup(resp.content, 'html.parser')

forecasts = page.find(id='seven-day-forecast-container')
data_containers = forecasts.findAll(class_='tombstone-container')

periods = []
description = []
temperature = []

for container in data_containers:
    period = container.find(class_='period-name').get_text()
    desc = container.img['alt']
    temp = container.find(class_='temp').get_text()

    periods.append(period)
    description.append(desc)
    temperature.append(temp)

df = pd.DataFrame({'Period':periods, 'Description':description, 'Temperature':temperature})

print(df)

