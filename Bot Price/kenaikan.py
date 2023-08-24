import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('api_key')
API_URL = os.getenv('api_url')

params = {
    'start': '1',
    'limit': '10',  # Ubah sesuai kebutuhan
    'convert': 'USD',
    'sort': 'percent_change_24h'  # Mengurutkan berdasarkan persentase perubahan harga dalam 24 jam
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

response = requests.get(API_URL, params=params, headers=headers)
data = response.json()

if response.status_code == 200:
    print("Kripto dengan kenaikan harga:")
    for crypto in data['data']:
        name = crypto['name']
        symbol = crypto['symbol']
        percent_change_24h = crypto['quote']['USD']['percent_change_24h']
        if percent_change_24h is not None and percent_change_24h > 0:
            print(f"{name} ({symbol}): +{percent_change_24h:.2f}%")
else:
    print("Error:", data['status']['error_message'])
