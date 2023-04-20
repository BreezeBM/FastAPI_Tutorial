# 코루틴 hello world
# https://docs.python.org/ko/3/library/asyncio-task.html
import asyncio


async def hello_world():
    await print("Hello World!")  # print에는 async를 붙일 수 없다. 어웨이터블 객체가 아님
    return 123


if __name__ == "__main__":
    asyncio.run(hello_world())
