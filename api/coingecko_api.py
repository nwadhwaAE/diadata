import requests

# Function to fetch price data from CoinGecko API
def fetch_coingecko_price(contract_address, chain):
    url = ''
    # Checking the chain and setting the URL and parameters accordingly
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
    # Sending a GET request to the CoinGecko API
    response = requests.get(url, params=params)
    
    # Checking the response status code
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching price data from CoinGecko API: {response.status_code}")
        return None