import requests_html
from bs4 import BeautifulSoup
import time
import datetime

def create_csv(filepath):
    with open(filepath, 'w') as csv_file:
        csv_file.write('date,time,last_price,change_percent\n')

oids = [334578, 334593, 334580, 334584, 334586, 334591, 334581, 334577, 334603, 334597, 334602]
url = 'https://www.avanza.se/marknadsoversikt.html'

session = requests_html.HTMLSession()
