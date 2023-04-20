import requests

# 이 친구는 동기적임


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    # url = "https://naver.com"
    urls = ["https//naver.com", "https://google.com", "https://inflearn.com"]

    # session = requests.Session()
    # session.get(url)
    # session.close()

    # 위의 세줄을 아래코드로 변경 가능
    with requests.Session() as session:
        # result = fetcher(session, urls)
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    main()
