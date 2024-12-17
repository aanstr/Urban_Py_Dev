import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for n in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар {n}')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Odin', 8))
    task2 = asyncio.create_task(start_strongman('Thor', 6))
    task3 = asyncio.create_task(start_strongman('Loki', 5))
    await task1
    await task2
    await task3


async def main():
    await start_tournament()

asyncio.run(main())
