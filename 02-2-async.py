import time
import asyncio

async def delivery(name, mealtime):
    print(f"{name}에게 배달완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")


# async =>  코루틴 함수
async def main():
    await asyncio.gather(
        await delivery("A", 10),
        await delivery("B", 3),
        await delivery("C", 4)
    )

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end-start)