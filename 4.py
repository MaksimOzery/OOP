# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:43:46 2020

@author: maksim
"""

import requests
from bs4 import BeautifulSoup
def spiders (max_list):
    page = 1
    while page <= max_list:
        url = 'https://elementy.ru/novosti_nauki/'
        source_code = requests.get(url)
        
        soup = BeautifulSoup(source_code.text, 'html.parser')
        print(soup)
        main_title = soup.find_all('a', {"class": "question__title-link"})
        for title in main_title:
            print(title.text.strip(), title.get('href')) 
        page+=1

trade_spiders(1)