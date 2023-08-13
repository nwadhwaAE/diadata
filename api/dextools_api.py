import requests
import os

# Function to fetch price data from DEXTools API
def fetch_dextools_price(chain, address):
    url = 'https://api.dextools.io/v1/token'
    params = {
        'chain': chain,
        'address': address
    }
    # Setting the API key in the headers
    headers = {
        'accept': 'application/json',
        'X-API-Key': os.environ.get('DEXTTOOLS_API_KEY')  # Using the secret as environment variable
    }
    # Sending a GET request to the DEXTools API
    response = requests.get(url, params=params, headers=headers)
    
    # Checking the response status code
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching price data from DEXTools API: {response.status_code}")
        return None