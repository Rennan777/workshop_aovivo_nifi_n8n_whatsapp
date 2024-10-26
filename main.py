import requests
from tinydb import TinyDB, Query
from datetime import datetime

db = TinyDB('banco_de_dados.json')

def get_price():
    url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
    response = requests.get(url)
    return response.json()

def calculate_kpis(price_data):
    #
    price_usd = float(price_data['data']['amount'])

    return price_usd

db.insert({**response.json(), 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})


