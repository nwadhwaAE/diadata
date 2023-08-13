import os
import requests

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1140170269244272672/uZLG8NMwRpu2aWuqVQ9uQqdISGsFpSgR8SsVPkxE0hFts1FymGkfyx2JEhPmEETIDbk0"

def send_discord_message(fantom_dextools_msg, fantom_coingecko_msg, polygon_dextools_msg, polygon_coingecko_msg):
    message = f"Fantom MiMATIC price comparison:\n"
    message += f"DIA vs DEXTools: {fantom_dextools_msg}\n"
    message += f"DIA vs CoinGecko: {fantom_coingecko_msg}\n\n"
    message += f"Polygon MiMATIC price comparison:\n"
    message += f"DIA vs DEXTools: {polygon_dextools_msg}\n"
    message += f"DIA vs CoinGecko: {polygon_coingecko_msg}"

    data = {
        "content": message
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("Message sent to Discord successfully.")
    else:
        print(f"Failed to send message to Discord. Status code: {response.status_code}")

