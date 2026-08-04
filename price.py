import requests
import time

SYMBOL = "BTCUSDT"

BINANCE_URL = "https://api.binance.com/api/v3/ticker/price"


def get_btc_price():
    try:
        response = requests.get(
            BINANCE_URL,
            params={"symbol": SYMBOL},
            timeout=10
        )

        data = response.json()

        if "price" not in data:
            print("Binance response:", data)
            return None

        return float(data["price"])

    except Exception as e:
        print("Price error:", e)
        return None


def get_price_change(start_price, current_price):

    if start_price is None or current_price is None:
        return 0

    if start_price == 0:
        return 0

    change = (
        (current_price - start_price)
        / start_price
    ) * 100

    return round(change, 4)


if __name__ == "__main__":

    print("Shuja Pro AI Price Engine Started")

    start = get_btc_price()

    print("Starting BTC Price:", start)

    while True:

        current = get_btc_price()

        if current is not None:
            change = get_price_change(start, current)
            print("BTC:", current, "Change:", change, "%")

        time.sleep(5)
