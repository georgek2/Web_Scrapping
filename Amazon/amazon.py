
import requests
from bs4 import BeautifulSoup


URL = 'https://www.amazon.com/Fifine-Microphone-Condenser-Recordings-YouTube/dp/B01D4HTIOY/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1530240151&sr=1-5&keywords=fifine+mic&linkCode=sl1&tag=techsource02-20&linkId=4eb269c41ab34ce7e688b141a449057d'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

para = soup.find_all('h3')

print(para)
print('Hello World')
