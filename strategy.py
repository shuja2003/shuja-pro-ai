# Shuja Pro AI v1
# Strategy and confidence engine

from config import CONFIDENCE_THRESHOLD


def calculate_confidence(
    trend_score,
    rsi_score,
    macd_score,
    atr_score,
    volume_score
):
    """
    Combine all signals into confidence score
    """

    total = (
        trend_score
        + rsi_score
        + macd_score
        + atr_score
        + volume_score
    )

    return min(total, 100)


def get_signal(
    confidence,
    direction
):
    """
    Final trading decision
    """

    if confidence >= CONFIDENCE_THRESHOLD:

        if direction == "BUY":
            return "🟢 BUY"

        elif direction == "SELL":
            return "🔴 SELL"


    return "⚪ NO TRADE"


def analyze_market(data):
    """
    Placeholder for full AI analysis.

    Later we will connect:
    - EMA trend
    - RSI
    - MACD
    - ATR
    - Volume
    - Order book
    - Trade flow
    """

    trend_score = 25
    rsi_score = 15
    macd_score = 15
    atr_score = 10
    volume_score = 10

    confidence = calculate_confidence(
        trend_score,
        rsi_score,
        macd_score,
        atr_score,
        volume_score
    )

    direction = "SELL"

    signal = get_signal(
        confidence,
        direction
    )

    return {
        "signal": signal,
        "confidence": confidence
    }
