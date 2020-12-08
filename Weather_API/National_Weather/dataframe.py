import pandas as pd
import requests 
from bs4 import BeautifulSoup as soup 

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324')

page_soup = soup(page.content, 'html.parser')

seven_day = page_soup.find(id='seven-day-forecast-container')

# Using CSS selector
period_tags = seven_day.select(".tombstone-container .period-name")
temp_tags = seven_day.select(".tombstone-container .temp")
short_descs = seven_day.select(".tombstone-container .short-desc")
desc_tags = seven_day.select(".tombstone-container img")

# List comprehensions to store the data we collect
periods = [pt.get_text() for pt in period_tags]
temps = [temp.get_text() for temp in temp_tags]
short = [sd.get_text() for sd in short_descs]
descs = [d['title'] for d in desc_tags]

# Creating the dataframe from the list comprehensions
df = pd.DataFrame({'periods': periods, 'short_desc': short, 'temperatures': temps, 'description':descs})

print(df)