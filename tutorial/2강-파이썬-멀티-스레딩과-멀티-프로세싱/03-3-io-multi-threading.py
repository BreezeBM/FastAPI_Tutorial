# https://docs.python.org/3.7/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


# 멀티스레딩
def fetcher(params):
    # print(params)
    session = params[0]
    url = params[1]

    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")

    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://apple.com", "https://google.com", "https://github.com"]

    executor = ThreadPoolExecutor(max_workers=1)  # 최대 실행할 스레드

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)

        params = [(session, url) for url in urls]  # 튜플이 만들어짐

        results = list(executor.map(fetcher, params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
