import asyncio
async def sqr(n):
    await asyncio.sleep(2)
    return n*n
async def main():
    results = await asyncio.gather(
        sqr(2),
        sqr(3),
        sqr(4)
    )
    print(results)

asyncio.run((main()))