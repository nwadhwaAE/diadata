import os
import requests

# Get the Discord Webhook URL from environment variables
DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL') 

# Function to send a message to Discord
def send_discord_message(message):
    data = {
        "content": message
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("Message sent to Discord successfully.")
    else:
        print(f"Failed to send message to Discord. Status code: {response.status_code}")

# Function to send comparison message to Discord
def discord_message_comparison(fantom_dextools_msg, fantom_coingecko_msg, polygon_dextools_msg, polygon_coingecko_msg):
    message = (
        f"**\n"
        f"Fantom MiMATIC price comparison:\n"
        f"DIA vs DEXTools: {fantom_dextools_msg}\n"
        f"DIA vs CoinGecko: {fantom_coingecko_msg}\n\n"
        f"Polygon MiMATIC price comparison:\n"
        f"DIA vs DEXTools: {polygon_dextools_msg}\n"
        f"DIA vs CoinGecko: {polygon_coingecko_msg}\n"
        f"**\n\n"
        f"*Inconsistency in prices on fantom:: Multichain has suffered a force majeure event, an exploit, and unauthorized withdrawals on 24/7. These events have led to the removal of the backing of most assets used within Fantom DeFi.*"
    )

    send_discord_message(message)

# Function to send price message to Discord
def discord_message_price(dia_fantom_price, dia_polygon_price, 
        dextools_fantom_price, dextools_polygon_price,
        coingecko_fantom_price, coingecko_polygon_price):
    message = (
        f"**\n"
        f"MiMATIC DIA price:\n"
        f"Fantom: {dia_fantom_price:.2f}\n"
        f"Polygon: {dia_polygon_price:.2f}\n\n"
        f"MiMATIC Dextools price:\n"
        f"Fantom: {dextools_fantom_price:.2f}\n"
        f"Polygon: {dextools_polygon_price:.2f}\n\n"
        f"MiMATIC Coingecko price:\n"
        f"Fantom: {coingecko_fantom_price:.2f}\n"
        f"Polygon: {coingecko_polygon_price:.2f}\n"
        f"**\n"
    )

    send_discord_message(message)