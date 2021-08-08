# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:12:20 2021

@author: Yashar
"""

import bs4
import requests
import pandas as pd
from datetime import datetime as dt
import pygsheets
from os import path, mkdir

# Service file containing authorization info to access Google Sheets API
SERVICE_FILE = 'coins-312914-cf31675474f9.json'
# Google Sheet name
SHEET_NAME = 'Coins'
# Website providing the coin prices
URL = 'https://arzdigital.com/coins/'


def get_coin_list(service_file: str, google_sheet_name: str,
                  working_sheet_name: str, col: str) -> set:
    """ Returns the list of all the coins you have in the sheet"""

    gc = pygsheets.authorize(service_file=service_file)
    g_sheet = gc.open(google_sheet_name)
    wks = g_sheet.worksheet('title', working_sheet_name)
    col_address = wks.range(col)
    coin_list = []
    for item in col_address:
        if item[0].value:
            coin_list.append(item[0].value)
    return set(coin_list[1:])


def single_coin(name: str, base_url: str = URL):
    """
    Parameters
    ----------
    name : str
        Name of the coin to get the price for.
    base_url : str, optional
        The url to the website providing the prices. The default is URL.
    Returns
    -------
    list
        A list containing coin name,
        price in USD and price in Rial in that order.
    """
    url = base_url + name + '/'
    r = requests.get(url)
    data = r.content
    soup = bs4.BeautifulSoup(data, 'html.parser')
    if soup.find('div', ['arz-coin-page-data__coin-price']):
        price = soup.find('div', ['arz-coin-page-data__coin-price']).text
        rial_price = soup.find('div',
                               ['arz-coin-page-data__coin-toman-price']).text
        return [name, price, rial_price]
    else:
        print('{} name not found on website!'.format(name))
        return [name, 'Coin not found!', 'Coin not found!']


coin_set = get_coin_list(SERVICE_FILE, SHEET_NAME, 'Sheet1', 'B:B')

""" Append the latest price of all the coins,
print a line on the console to show progress."""
temp = []
for item in coin_set:
    print('Getting the price of {} ...'.format(item))
    temp.append(single_coin(item))

""" Put all the captured prices in a DataFrame for easier handling."""
df = pd.DataFrame(columns=['name', 'price', 'rial_price'], data=temp)

# Clean the data by removing signs and commas
df.price = df.price.apply(lambda x: float(x.replace('$', '').replace(',', '')))
df.rial_price = df.rial_price.apply(lambda x: float(
                                    x.replace('تومان', '').replace(',', '')))

""" Save a copy of the price lists to local machine as an Excel file."""
if not path.exists('./HistoricalData/'):
    mkdir('HistoricalData')
df.to_excel('./HistoricalData/Coin_price_{}.xlsx'.format(dt.today().strftime('%Y-%m-%d')), index=False)

"""
 Add the captured list to the google sheet
 The authorization file should be in the same folder
 This will overwrite the second sheet of the Spreadsheet,
 Make sure the list stays as the second sheet
"""
gc = pygsheets.authorize(service_file=SERVICE_FILE)
sh = gc.open(SHEET_NAME)
wks = sh.worksheet('title', 'Price List')
wks.set_dataframe(df, (1, 1))
wks.update_value('F1', dt.now().strftime('%Y-%m-%d %H:%M'))
