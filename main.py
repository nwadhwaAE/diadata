# Import functions from API modules and Discord integration
from api import fetch_fantom_mimatic_price, fetch_polygon_mimatic_price, fetch_coingecko_price, fetch_dextools_price
from utils import calculate_divergence, highlight_divergence, discord_message_comparison,discord_message_price

fantom_addr = "0xfb98b335551a418cd0737375a2ea0ded62ea213b"
polygon_addr = "0xa3fa99a148fa48d14ed51d610c367c61876997f1"

# Fetch prices from different APIs
fantom_dia_data = fetch_fantom_mimatic_price()
polygon_dia_data = fetch_polygon_mimatic_price()
coingecko_fantom_data = fetch_coingecko_price(fantom_addr, 'fantom')
coingecko_polygon_data = fetch_coingecko_price(polygon_addr, 'polygon')
dextools_fantom_data = fetch_dextools_price('fantom', fantom_addr)
dextools_polygon_data = fetch_dextools_price('polygon', polygon_addr)


# Check if data was fetched successfully from all APIs
if fantom_dia_data and polygon_dia_data and coingecko_fantom_data and coingecko_polygon_data and dextools_fantom_data and dextools_polygon_data:
    # Extract prices from fetched data
    dia_fantom_price = fantom_dia_data['Price']
    dia_polygon_price = polygon_dia_data['Price']
    coingecko_fantom_price = coingecko_fantom_data[fantom_addr]['usd']
    coingecko_polygon_price = coingecko_polygon_data[0]['current_price']
    dextools_fantom_price = dextools_fantom_data['data']['reprPair']['price']
    dextools_polygon_price = dextools_polygon_data['data']['reprPair']['price']

    # Send prices to Discord
    discord_message_price(
        dia_fantom_price, dia_polygon_price, 
        dextools_fantom_price, dextools_polygon_price,
        coingecko_fantom_price, coingecko_polygon_price
    )

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
    discord_message_comparison(
        dia_vs_dextools_fantom_highlight,
        dia_vs_coingecko_fantom_highlight,
        dia_vs_dextools_polygon_highlight,
        dia_vs_coingecko_polygon_highlight
    )

    print("Results sent to Discord.")

else:
    print("Failed to fetch price data from one or more sources.")
