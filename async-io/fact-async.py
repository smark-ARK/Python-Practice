import asyncio


async def factorial(name, num):
    f = 1
    for i in range(2, num + 1):
        print(f"running task:{name} | value of i is {i}")
        await asyncio.sleep(1)
        f *= i
    return f


async def main():
    out = await asyncio.gather(factorial("A", 2), factorial("B", 55), factorial("C", 8))
    return out


print(asyncio.run(main()))
