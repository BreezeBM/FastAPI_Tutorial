from typing import Optional
from fastapi import FastAPI


# 싱글톤 패턴
# FastAPI 클래스를 가져와서 app이라는 것 자체가 핵심적인 인스턴스
app = FastAPI()


# Controller?


# 데코레이터 패턴, 함수에 함수를 꾸며주는 방식
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def read_root():
    print("HELLO FASTAPI")
    return {"Hello": "FastAPI"}


# q: Query를 말함
# http://localhost:8000/items/123?q=hello
# {"item_id":123,"q":"hello"}
@app.get("/items/{item_id}/{xyz}")
def read_item(item_id: int, xyz: str, q: Optional[str] = None):
    return {"item_id": item_id, "xyz": xyz, "q": q}
