import requests

def fetch_dextools_price(chain, address):
    url = 'https://api.dextools.io/v1/token'
    params = {
        'chain': chain,
        'address': address
    }
    
    headers = {
        'accept': 'application/json',
        'X-API-Key': '0e9a4183bea257909e28e54846483563'
    }
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching price data from DEXTools API: {response.status_code}")
        return None
