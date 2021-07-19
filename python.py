import requests

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR API KEY'
}

params = {
    'start': '1',
    'limit': '3',
    'convert': 'USDT'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

req = requests.get(url, params=params, headers=headers).json()

data = req['data']

print("COIN - PRICE - MARKET CAP")

for i in data:
  print(i['symbol'], "  ", int(i['quote']['USDT']['price']), "  ", int(i['quote']['USDT']['market_cap']), "USDT")