import requests
from bs4 import BeautifulSoup as soup 
import pandas as pd 

resp = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.X4QHXtAza00')

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

