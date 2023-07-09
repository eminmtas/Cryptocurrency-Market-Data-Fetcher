# Cryptocurrency Market Data Fetcher

Cryptocurrency Market Data Fetcher is an advanced, lightweight Python program that fetches and displays the top three cryptocurrencies based on their market capitalization. It utilizes the robust and comprehensive CoinMarketCap API to obtain real-time data.

## Features

- Fetches real-time data for top 3 cryptocurrencies.
- Displays the 'Symbol', 'Price' and 'Market Cap' in USDT (Tether) for each of these cryptocurrencies.
- Easy to modify parameters to display more cryptocurrencies or alter the currency conversion.

## Getting Started

1. Clone this repository: `git clone https://github.com/eminmtas/cryptocurrencyAPI`
2. Install the required Python dependencies: `pip install -r requirements.txt`
3. Acquire a free API Key from [CoinMarketCap](https://pro.coinmarketcap.com).
4. Open `main.py` and replace `'YOUR_API_KEY'` with the API Key you obtained in step 3.
5. Run the script: `python main.py`

## Customization

The script is currently set to fetch data for the top 3 cryptocurrencies. However, you can modify this to fetch data for more or less cryptocurrencies by simply changing the 'limit' parameter in `self.params` within the `CryptoData` class.

In addition, you can also alter the currency conversion from 'USDT' (Tether) to any other supported currency by changing the 'convert' parameter in `self.params`.
