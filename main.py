from dia_api import fetch_fantom_mimatic_price, fetch_polygon_mimatic_price
from coingecko_api import fetch_coingecko_price
from dextools_api import fetch_dextools_price

def highlight_divergence(price1, price2, threshold_percent):
    divergence = abs(price1 - price2) / price1 * 100
    if divergence > threshold_percent:
        return f"Divergence: {divergence:.2f}%"
    else:
        return "No significant divergence"

# Fetch prices from different APIs
fantom_dia_data = fetch_fantom_mimatic_price()
polygon_dia_data = fetch_polygon_mimatic_price()
coingecko_fantom_data = fetch_coingecko_price('0xfb98b335551a418cd0737375a2ea0ded62ea213b', 'fantom')
coingecko_polygon_data = fetch_coingecko_price('0xa3fa99a148fa48d14ed51d610c367c61876997f1', 'polygon')
dextools_fantom_data = fetch_dextools_price('fantom', '0xfb98b335551a418cd0737375a2ea0ded62ea213b')
dextools_polygon_data = fetch_dextools_price('polygon', '0xa3fa99a148fa48d14ed51d610c367c61876997f1')

if fantom_dia_data and polygon_dia_data and coingecko_fantom_data and coingecko_polygon_data and dextools_fantom_data and dextools_polygon_data:
    dia_fantom_price = fantom_dia_data['Price']
    dia_polygon_price = polygon_dia_data['Price']
    coingecko_fantom_price = coingecko_fantom_data['0xfb98b335551a418cd0737375a2ea0ded62ea213b']['usd']
    coingecko_polygon_price = coingecko_polygon_data[0]['current_price']
    dextools_fantom_price = dextools_fantom_data['data']['reprPair']['price']
    dextools_polygon_price = dextools_polygon_data['data']['reprPair']['price']
    
    print("Fantom MiMATIC price comparison:")
    print("DIA vs DEXTools:", highlight_divergence(dia_fantom_price, dextools_fantom_price, 5))
    print("DIA vs CoinGecko:", highlight_divergence(dia_fantom_price, coingecko_fantom_price, 5))
    
    print("\nPolygon MiMATIC price comparison:")
    print("DIA vs DEXTools:", highlight_divergence(dia_polygon_price, dextools_polygon_price, 5))
    print("DIA vs CoinGecko:", highlight_divergence(dia_polygon_price, coingecko_polygon_price, 5))
    
else:
    print("Failed to fetch price data from one or more sources.")
