# Import functions from API modules and Discord integration
from api.dia_api import fetch_fantom_mimatic_price, fetch_polygon_mimatic_price
from api.coingecko_api import fetch_coingecko_price
from api.dextools_api import fetch_dextools_price
from utils.comparison import calculate_divergence, highlight_divergence
from utils.discord_integration import send_discord_message



# Fetch prices from different APIs
fantom_dia_data = fetch_fantom_mimatic_price()
polygon_dia_data = fetch_polygon_mimatic_price()
coingecko_fantom_data = fetch_coingecko_price('0xfb98b335551a418cd0737375a2ea0ded62ea213b', 'fantom')
coingecko_polygon_data = fetch_coingecko_price('0xa3fa99a148fa48d14ed51d610c367c61876997f1', 'polygon')
dextools_fantom_data = fetch_dextools_price('fantom', '0xfb98b335551a418cd0737375a2ea0ded62ea213b')
dextools_polygon_data = fetch_dextools_price('polygon', '0xa3fa99a148fa48d14ed51d610c367c61876997f1')

# Check if data was fetched successfully from all APIs
if fantom_dia_data and polygon_dia_data and coingecko_fantom_data and coingecko_polygon_data and dextools_fantom_data and dextools_polygon_data:
    # Extract prices from fetched data
    dia_fantom_price = fantom_dia_data['Price']
    dia_polygon_price = polygon_dia_data['Price']
    coingecko_fantom_price = coingecko_fantom_data['0xfb98b335551a418cd0737375a2ea0ded62ea213b']['usd']
    coingecko_polygon_price = coingecko_polygon_data[0]['current_price']
    dextools_fantom_price = dextools_fantom_data['data']['reprPair']['price']
    dextools_polygon_price = dextools_polygon_data['data']['reprPair']['price']

    # Calculate divergences for different pairs
    dia_vs_dextools_fantom_divergence = calculate_divergence(dia_fantom_price, dextools_fantom_price)
    dia_vs_coingecko_fantom_divergence = calculate_divergence(dia_fantom_price, coingecko_fantom_price)
    dia_vs_dextools_polygon_divergence = calculate_divergence(dia_polygon_price, dextools_polygon_price)
    dia_vs_coingecko_polygon_divergence = calculate_divergence(dia_polygon_price, coingecko_polygon_price)

    # Highlight divergences based on threshold and store the results
    dia_vs_dextools_fantom_highlight = highlight_divergence(dia_vs_dextools_fantom_divergence, 5)
    dia_vs_coingecko_fantom_highlight = highlight_divergence(dia_vs_coingecko_fantom_divergence, 5)
    dia_vs_dextools_polygon_highlight = highlight_divergence(dia_vs_dextools_polygon_divergence, 5)
    dia_vs_coingecko_polygon_highlight = highlight_divergence(dia_vs_coingecko_polygon_divergence, 5)

    # Send results to Discord
    send_discord_message(
        dia_vs_dextools_fantom_highlight,
        dia_vs_coingecko_fantom_highlight,
        dia_vs_dextools_polygon_highlight,
        dia_vs_coingecko_polygon_highlight
    )

    print("Results sent to Discord.")

else:
    print("Failed to fetch price data from one or more sources.")
