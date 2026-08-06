import asyncio
import websockets
import json


URL = "wss://ws-live-data.polymarket.com"


async def main():

    print("Connecting to Polymarket RTDS...", flush=True)

    async with websockets.connect(URL) as ws:

        print("✅ Connected to Polymarket RTDS", flush=True)

        subscribe = {
            "action": "subscribe",
            "subscriptions": [
                {
                    "topic": "crypto_prices",
                    "type": "BTC"
                }
            ]
        }

        await ws.send(json.dumps(subscribe))

        print("📡 Subscription sent", flush=True)

        try:
            for i in range(5):
                message = await ws.recv()

                print("\n--- MESSAGE ---", flush=True)
                print(message, flush=True)

        except Exception as e:
            print("❌ Error receiving data:", e, flush=True)

        print("\n✅ Test completed", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
