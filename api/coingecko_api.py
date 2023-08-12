import requests

def fetch_coingecko_price(contract_address, chain):
    url = ''
    if chain == 'fantom':
        url += 'https://api.coingecko.com/api/v3/simple/token_price/fantom'
        params = {
            'contract_addresses': contract_address,
            'vs_currencies': 'usd'
        }
    elif chain == 'polygon':
        url += 'https://api.coingecko.com/api/v3/coins/markets'
        params = {
            'vs_currency': 'usd',
            'ids': 'mimatic'
        }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching price data from CoinGecko API: {response.status_code}")
        return None
