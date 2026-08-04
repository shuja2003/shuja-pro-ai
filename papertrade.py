# Shuja Pro AI v1
# Paper Trading Engine

import time
from datetime import datetime


balance = 1000
open_trade = None

wins = 0
losses = 0


def open_paper_trade(
    direction,
    price,
    confidence
):
    global open_trade

    open_trade = {
        "direction": direction,
        "entry": price,
        "confidence": confidence,
        "time": datetime.now()
    }

    print("Paper Trade Opened")
    print(open_trade)


def close_paper_trade(exit_price):
    global open_trade
    global balance
    global wins
    global losses

    if open_trade is None:
        return

    entry = open_trade["entry"]
    direction = open_trade["direction"]

    if direction == "BUY":
        profit = (
            (exit_price - entry)
            / entry
        ) * 100

    else:
        profit = (
            (entry - exit_price)
            / entry
        ) * 100


    if profit > 0:
        wins += 1
        result = "WIN"

    else:
        losses += 1
        result = "LOSS"


    print("\nTrade Closed")
    print("Result:", result)
    print("Profit:", round(profit, 3), "%")
    print(
        "Wins:",
        wins,
        "Losses:",
        losses
    )

    open_trade = None


def get_statistics():

    total = wins + losses

    if total == 0:
        win_rate = 0

    else:
        win_rate = (
            wins / total
        ) * 100


    return {
        "Total Trades": total,
        "Wins": wins,
        "Losses": losses,
        "Win Rate": round(
            win_rate, 2
        )
    }
