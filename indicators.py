import pandas as pd


def calculate_ema(data, period):
    """
    Calculate Exponential Moving Average
    """
    return data.ewm(
        span=period,
        adjust=False
    ).mean()


def calculate_rsi(data, period=14):
    """
    Calculate RSI
    """

    delta = data.diff()

    gain = delta.where(
        delta > 0, 0
    )

    loss = -delta.where(
        delta < 0, 0
    )

    avg_gain = gain.rolling(
        period
    ).mean()

    avg_loss = loss.rolling(
        period
    ).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (
        100 / (1 +
