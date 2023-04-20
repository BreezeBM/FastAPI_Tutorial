# pip install aiohttp~=3.7.3
import asyncio

import aiohttp


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https//naver.com", "https://google.com", "https://inflearn.com"]

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        # result = await fetcher(session, urls[0])
        print(result)
        pass


if __name__ == "__main__":
    asyncio.run(main())
