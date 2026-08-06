import requests

URL = "https://gamma-api.polymarket.com/markets"

response = requests.get(URL, timeout=20)

print("Status Code:", response.status_code)

data = response.json()

print("Type:", type(data))

if isinstance(data, list):
    print("Number of items:", len(data))
    if len(data) > 0:
        print("First item:")
        print(data[0])
else:
    print(data)
