from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    # 컬렉션 이름을 지정
    class Config:
        collection = "books"
