import asyncio

async def print1():
    print(1)

async def print2():
    await asyncio.sleep(3)
    (print(2))

async def print3():
    print(3)

async def main():

    task_1 = asyncio.create_task(print1())
    task_2 = asyncio.create_task(print2())
    task_3 = asyncio.create_task(print3())

    await asyncio.gather(task_1, task_2, task_3)

if __name__ == '__main__':
    asyncio.run(main())

