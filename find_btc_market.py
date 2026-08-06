import asyncio
from polymarket import AsyncPublicClient


async def main():

    print("Connecting to Polymarket API...", flush=True)

    async with AsyncPublicClient() as client:

        print("✅ Connected", flush=True)

        markets = client.list_markets(closed=False)

        found = 0

        async for market in markets.iter_items():

            question = market.question.lower()

            if "bitcoin" in question or "btc" in question:

                found += 1

                print("\n====================", flush=True)
                print("QUESTION:", market.question, flush=True)
                print("MARKET ID:", market.id, flush=True)

                print("TOKENS:", flush=True)
                print(market.tokens, flush=True)

                if found >= 10:
                    break

        print("\n✅ Search completed", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
