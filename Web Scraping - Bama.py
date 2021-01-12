# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:35:56 2020

@author: Yashar
"""
import requests
from bs4 import BeautifulSoup as bs
import re
import mysql.connector

#%%
car_name = input()
r = requests.get('https://divar.ir/s/tehran/car?q='+car_name)

soup = bs(r.text, 'html.parser')
result = []
cars = soup.find_all('div', attrs = {'class':'listdata'})
for car in cars:    
    name = re.sub('\s','', car.find('a', attrs = {'class':'cartitle cartitle-desktop'}).find('h2').text)
    price = car.find('span', attrs= {'itemprop':'price'}).text
#    age = re.sub('\s', '', car.find('p', attrs = {'class':'price milage-text-mobile visible-xs price-milage-mobile'}).text)
#    age = re.sub('کارکرد', '', age)
    result.append((name, price))
