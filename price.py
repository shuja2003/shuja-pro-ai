# Shuja Pro AI v2
# Price and Candle Engine

import requests
import pandas as pd


SYMBOL = "BTCUSDT"
INTERVAL = "5m"
LIMIT = 200


PRICE_URL = (
    "https://data-api.binance.vision/api/v3/ticker/price"
)

KLINES_URL = (
    "https://data-api.binance.vision/api/v3/klines"
)


def get_btc_price():

    try:
        response = requests.get(
            PRICE_URL,
            params={
                "symbol": SYMBOL
            },
            timeout=10
        )

        data = response.json()

        if "price" not in data:
            print("Price response:", data)
            return None

        return float(data["price"])

    except Exception as e:
        print("Price error:", e)
        return None



def get_candles():

    try:
        response = requests.get(
            KLINES_URL,
            params={
                "symbol": SYMBOL,
                "interval": INTERVAL,
                "limit": LIMIT
            },
            timeout=10
        )

        rows = response.json()

        df = pd.DataFrame(
            rows,
            columns=[
                "time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
                "quote_volume",
                "trades",
                "buy_volume",
                "buy_quote",
                "ignore"
            ]
        )


        for col in [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]:
            df[col] = df[col].astype(float)


        return df


    except Exception as e:
        print("Candle error:", e)
        return None



def get_price_change(start_price, current_price):

    if (
        start_price is None
        or current_price is None
        or start_price == 0
    ):
        return 0


    change = (
        (current_price - start_price)
        / start_price
    ) * 100


    return round(change, 4)
