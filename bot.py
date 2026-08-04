# Shuja Pro AI v2
# Main Bot Controller

import time

from price import (
    get_btc_price,
    get_candles
)

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


        candles = get_candles()

        if candles is None:
            print("No candle data")
            time.sleep(10)
            continue


        analysis = analyze_market(
            candles
        )


        signal = analysis["signal"]
        confidence = analysis["confidence"]


        print("\nBTC Price:", price)
        print("Signal:", signal)
        print("Confidence:", confidence)


        send_message(
            f"""
🤖 Shuja Pro AI

BTCUSDT

Price: {price}

Signal: {signal}

Confidence: {confidence}%

Mode:
PAPER TRADING
"""
        )


        if signal == "🟢 BUY" or signal == "🔴 SELL":

            direction = (
                "BUY"
                if signal == "🟢 BUY"
                else "SELL"
            )


            open_paper_trade(
                direction,
                price,
                confidence
            )


            time.sleep(60)


            exit_price = get_btc_price()


            if exit_price:

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
