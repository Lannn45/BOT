import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('api_key')
API_URL = os.getenv('api_url')

params = {
    'start':'1',
    'limit':'1000',  # Ubah sesuai kebutuhan
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

response = requests.get(API_URL, params=params, headers=headers)
data = response.json()

if response.status_code == 200:
    for crypto in data['data']:
        name = crypto['name']
        symbol = crypto['symbol']
        price = crypto['quote']['USD']['price']
        print(f"{name} ({symbol}): ${price:.2f}")
else:
    print("Error:", data['status']['error_message'])
