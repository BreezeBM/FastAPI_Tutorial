import asyncio

import aiohttp
import requests
import time
import os
import threading


# os.getpid : 현재 프로세스의 id를 반환
async def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    async with session.get(url) as response:
        return await response.text


async def main():
    # 애플로 요청을 보내고 fetcher에서 await으로 탈출
    # 구글이라는 코루틴으로 들어가서 탈출
    # urls = ["https://apple.com", "https://google.com", "https://github.com"]
    urls = ["https://apple.com"]

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
