# Shuja Pro AI v1
# Telegram Message Module

import os
import requests


TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN"
)

CHAT_ID = os.getenv(
    "CHAT_ID"
)


def send_message(message):

    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Telegram credentials missing")
        return

    url = (
        f"https://api.telegram.org/"
        f"bot{TELEGRAM_TOKEN}/sendMessage"
    )

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        print(
            "Telegram response:",
            response.text
        )

    except Exception as e:
        print(
            "Telegram error:",
            e
        )
