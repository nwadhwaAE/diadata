import requests

def fetch_mimatic_price(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching MiMatic price data:", response.status_code)
        return None

def fetch_fantom_mimatic_price():
    fantom_endpoint = "https://api.diadata.org/v1/assetQuotation/Fantom/0xfb98b335551a418cd0737375a2ea0ded62ea213b"
    return fetch_mimatic_price(fantom_endpoint)

def fetch_polygon_mimatic_price():
    polygon_endpoint = "https://api.diadata.org/v1/assetQuotation/Polygon/0xa3Fa99A148fA48D14Ed51d610c367C61876997F1"
    return fetch_mimatic_price(polygon_endpoint)