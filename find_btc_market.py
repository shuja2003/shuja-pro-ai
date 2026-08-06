import requests


URL = "https://gamma-api.polymarket.com/markets"


def main():

    print("Fetching Polymarket markets...", flush=True)

    response = requests.get(
        URL,
        params={
            "closed": "false",
            "limit": 100
        },
        timeout=20
    )

    markets = response.json()

    found = 0

    for market in markets:

        question = market.get("question", "")

        if "bitcoin" in question.lower() or "btc" in question.lower():

            found += 1

            print("\n====================")
            print("QUESTION:")
            print(question)

            print("MARKET ID:")
            print(market.get("id"))

            print("TOKENS:")
            print(market.get("clobTokenIds"))

            if found >= 10:
                break

    print("\n✅ Done")


if __name__ == "__main__":
    main()
    
                
