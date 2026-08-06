import asyncio
from polymarket import AsyncPublicClient


async def main():

    async with AsyncPublicClient() as client:

        markets = client.list_markets(closed=False)

        async for market in markets.iter_items():

            question = market.question.lower()

            if "bitcoin" in question or "btc" in question:

                print("\nQUESTION:")
                print(market.question)

                print("MARKET ID:")
                print(market.id)

                print("TOKENS:")
                print(market.tokens)


if __name__ == "__main__":
    asyncio.run(main())
