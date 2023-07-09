import requests

# Create a CryptoData class to store the data and methods to get and print the data
class CryptoData:
    def __init__(self, api_key, conversion_currency='USDT'):
        self.api_key = api_key
        self.base_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key
        }
        self.params = {
            'start': '1',
            'limit': '3',
            'convert': conversion_currency
        }

    # Get the data
    def get_data(self):
        response = requests.get(self.base_url, params=self.params, headers=self.headers)
        response.raise_for_status()  # Error Handling
        return response.json()['data']

    # Helper function to format numbers with commas
    def intcomma(self, value):
        return "{:,}".format(value).replace(",", ".")

    # Print the data
    def print_crypto_data(self):
        data = self.get_data()
        print("{:<10} {:<10} {:<20}".format("COIN", "PRICE", "MARKET CAP"))
        for i in data:
            print("{:<10} {:<10} {:<20} USDT".format(i['symbol'], int(i['quote']['USDT']['price']), self.intcomma(int(i['quote']['USDT']['market_cap']))))

# Create a CryptoData object
crypto_data = CryptoData('YOUR_API_KEY')

# Print the data
crypto_data.print_crypto_data()
