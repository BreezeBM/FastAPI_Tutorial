import requests
import time
import os
import threading


# os.getpid : 현재 프로세스의 id를 반환
def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    # 애플에 요청을 보내고 응답받고 구글로 요청을 보내고...
    # urls = ["https://apple.com", "https://google.com", "https://github.com"]
    urls = ["https://apple.com"]

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
