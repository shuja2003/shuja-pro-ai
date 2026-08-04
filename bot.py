# Shuja Pro AI v1
# Main Bot Controller

import time

from price import get_btc_price
from strategy import analyze_market
from papertrade import (
    open_paper_trade,
    close_paper_trade,
    get_statistics
)
from telegram_bot import send_message


def run_bot():

    print("🚀 Shuja Pro AI Started")

    for _ in range(3):

        price = get_btc_price()

        if price is None:
            time.sleep(5)
            continue


        analysis = analyze_market(None)

        signal = analysis["signal"]
        confidence = analysis["confidence"]


        print("\nBTC Price:", price)
print("Signal:", signal)
print("Confidence:", confidence)

send_message(
    f"""🤖 Shuja Pro AI

BTCUSDT

Signal: {signal}

Confidence: {confidence}%

Mode: PAPER TRADING
"""
)


        if signal == "🟢 BUY":

            open_paper_trade(
                "BUY",
                price,
                confidence
            )

            time.sleep(60)

            exit_price = get_btc_price()

            close_paper_trade(
                exit_price
            )


            print(
                get_statistics()
            )


        else:
            print("No trade")


        time.sleep(60)



if __name__ == "__main__":
    run_bot()
