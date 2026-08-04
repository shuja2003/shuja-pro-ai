import csv
import os
from datetime import datetime

FILE_NAME = "trade_log.csv"


def save_trade(
    signal,
    entry_price,
    exit_price,
    result,
    profit,
    confidence
):

    file_exists = os.path.isfile(FILE_NAME)

    with open(
        FILE_NAME,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Time",
                "Signal",
                "Entry",
                "Exit",
                "Result",
                "Profit %",
                "Confidence"
            ])

        writer.writerow([
            datetime.now(),
            signal,
            entry_price,
            exit_price,
            result,
            round(profit, 3),
            confidence
        ])
