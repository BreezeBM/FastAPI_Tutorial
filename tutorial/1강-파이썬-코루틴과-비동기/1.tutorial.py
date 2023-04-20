# 비동기적...
import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)  # 해당하는 초 만큼 sleep
    print(f"{name} 식사완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")


# async def main():
#     await asyncio.gather(
#         delivery("A", 3),
#         delivery("B", 3),
#         delivery("C", 4),
#     )


async def main():
    await delivery("A", 3)
    await delivery("B", 3)
    await delivery("C", 4)


if __name__ == "__main__":
    start = time.time()  # 현재 시점을 찍기
    asyncio.run(main())
    end = time.time()  # main() 실행이 끝난 시점 찍기
    print(end - start)
