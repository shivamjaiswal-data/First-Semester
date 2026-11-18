import asyncio
async def mark_attd(st):
    print(f"marki st for {st}")
    await asyncio.sleep(4)
    print(f"{st} completed")


async def main ():
    task =await asyncio.gather(
        mark_attd("a"),
        mark_attd("n"),
        mark_attd("c"),
        mark_attd("asff")

) 
    print(task)

asyncio.run((main()))