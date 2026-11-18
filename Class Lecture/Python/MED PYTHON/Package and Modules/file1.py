# import asyncio 
# async def grret():
#     print("hello")
#     await asyncio.sleep(2)
#     print("Welcome to asyncio")
# asyncio.run((grret()))




# import asyncio

# async def fn():
#     print("thi is ")




import time
def task(name):
    print(f"{name} Started")
    time.sleep(3)
    print(f"{name} Completed")

task("Task1")
task("Task2")
task("Task3")
# asyncio.run((task()))
