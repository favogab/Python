# program that takes a number of bitcoins as a command-line argument 
# and converts it to USD using the CoinCap API.

import sys
import requests
import os

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

api_key = os.getenv("COINCAP_API_KEY")

if not api_key:
    sys.exit("Missing CoinCap API key")

url = "https://rest.coincap.io/v3/assets/bitcoin"

try:
    response = requests.get(
        url,
        params={"apiKey": api_key},
        timeout=10
    )
    response.raise_for_status()
    bitcoin_data = response.json()

except requests.RequestException:
    sys.exit("Could not retrieve Bitcoin price")

try:
    price = float(bitcoin_data["data"]["priceUsd"])
except (KeyError, TypeError, ValueError):
    sys.exit("Invalid Bitcoin price data")

total = bitcoins * price

print(f"${total:,.4f}")