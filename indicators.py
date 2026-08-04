# Shuja Pro AI v2
# Technical Indicators Engine

import pandas as pd


def calculate_ema(data, period):

    return data["close"].ewm(
        span=period,
        adjust=False
    ).mean()



def calculate_rsi(data, period=14):

    delta = data["close"].diff()

    gain = delta.clip(
        lower=0
    )

    loss = -delta.clip(
        upper=0
    )


    avg_gain = gain.rolling(
        period
    ).mean()

    avg_loss = loss.rolling(
        period
    ).mean()


    rs = avg_gain / avg_loss


    rsi = 100 - (
        100 / (1 + rs)
    )


    return rsi



def calculate_macd(data):

    ema_fast = data["close"].ewm(
        span=12,
        adjust=False
    ).mean()


    ema_slow = data["close"].ewm(
        span=26,
        adjust=False
    ).mean()


    macd = ema_fast - ema_slow


    signal = macd.ewm(
        span=9,
        adjust=False
    ).mean()


    return macd, signal



def calculate_volume_strength(data):

    avg_volume = data["volume"].mean()

    current_volume = data["volume"].iloc[-1]


    if avg_volume == 0:
        return 0


    return (
        current_volume / avg_volume
    )
