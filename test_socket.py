import asyncio
import websockets

URL = "wss://ws-live-data.polymarket.com"

async def main():

    print("Connecting to Polymarket RTDS...", flush=True)

    async with websockets.connect(URL) as ws:

        print("✅ Connected to Polymarket RTDS", flush=True)

        for i in range(5):
            message = await ws.recv()
            print(message, flush=True)

        print("✅ Test completed", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
