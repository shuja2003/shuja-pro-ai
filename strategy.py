# Shuja Pro AI v2
# Real Indicator Strategy

from config import CONFIDENCE_THRESHOLD
from indicators import (
    calculate_ema,
    calculate_rsi,
    calculate_macd,
    calculate_volume_strength
)


def analyze_market(data):

    if data is None:
        return {
            "signal": "⚪ NO TRADE",
            "confidence": 0
        }


    close = data["close"]


    ema50 = calculate_ema(
        data,
        50
    )

    ema200 = calculate_ema(
        data,
        200
    )


    rsi = calculate_rsi(
        data
    )


    macd, signal_line = calculate_macd(
        data
    )


    volume_strength = calculate_volume_strength(
        data
    )


    score = 0
    direction = "NONE"


    # Trend
    if ema50.iloc[-1] > ema200.iloc[-1]:
        score += 30
        direction = "BUY"

    elif ema50.iloc[-1] < ema200.iloc[-1]:
        score += 30
        direction = "SELL"


    # RSI
    if rsi.iloc[-1] > 50:
        score += 20

    elif rsi.iloc[-1] < 50:
        score += 20


    # MACD
    if macd.iloc[-1] > signal_line.iloc[-1]:
        score += 20

    else:
        score += 20


    # Volume
    if volume_strength > 1:
        score += 15


    confidence = min(
        score,
        100
    )


    if confidence >= CONFIDENCE_THRESHOLD:

        if direction == "BUY":
            final_signal = "🟢 BUY"

        elif direction == "SELL":
            final_signal = "🔴 SELL"

        else:
            final_signal = "⚪ NO TRADE"

    else:
        final_signal = "⚪ NO TRADE"


    return {
        "signal": final_signal,
        "confidence": confidence
    }
