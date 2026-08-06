# Polymarket RTDS Socket Test
# Shuja BTC 5M Bot

import asyncio
import websockets


URL = "wss://ws-live-data.polymarket.com"


async def main():

    print("Connecting to Polymarket RTDS...")

    try:
        async with websockets.connect(URL) as ws:

            print("✅ Connected to Polymarket RTDS")

            while True:
                message = await ws.recv()

                print("\n--- MESSAGE ---")
                print(message)

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    asyncio.run(main())
