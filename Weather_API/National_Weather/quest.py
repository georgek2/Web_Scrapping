
import requests 
from bs4 import BeautifulSoup as soup 

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.X2MCqmgza00')

page_soup = soup(page.content, 'html.parser')

seven_day = page_soup.find(id='seven-day-forecast-container')

forecast_items = seven_day.find_all(class_='tombstone-container')

tonight = forecast_items[0]

period = tonight.find(class_='period-name').get_text()
desc = tonight.img['title']
temp_low = tonight.find(class_='temp').get_text()
verdict = tonight.find(class_='short-desc').get_text()

print('Period: ', period)
print('Short Description: ', desc)
print('Temperature: ', temp_low)
print('Verdict: ', verdict)