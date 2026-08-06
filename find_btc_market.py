import requests
import json

URL = "https://gamma-api.polymarket.com/markets"

print("Fetching Polymarket markets...", flush=True)

r = requests.get(URL, timeout=20)

print("Status:", r.status_code, flush=True)

data = r.json()

print("Total received:", len(data), flush=True)

for market in data[:5]:
    print("====================")
    print(json.dumps(market, indent=2)[:1000])
