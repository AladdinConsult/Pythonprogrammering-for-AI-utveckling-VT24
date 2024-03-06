
import pyppdf.patch_pyppeteer
import requests_html
from bs4 import BeautifulSoup
import time 

url = 'https://www.avanza.se/marknadsoversikt.html'
energy_oid = '334578' 

session = requests_html.HTMLSession()
page_data = session.get(url)
page_data.html.render()

if page_data.ok:
    html = page_data.html.html
    soup = BeautifulSoup(html, 'html.parser')
    # Find the <tr> we are intrested in
    tr = soup.find('tr', {'data-oid': energy_oid, 'data-delayed':'true'})
    
    # Get the change percent
    change_percent = tr.find('td', {'class':'changePercent'}).text.strip()
    change_percent = change_percent.replace(',' , '.')
    change_percent = float(change_percent)

    # Get last price
    last_price = tr.find('td', {'class': 'lastPrice'}).text.strip()
    last_price = last_price.replace('\xa0', '').replace(',' , '.')
    last_price = float(last_price)

    print(last_price)

   
    