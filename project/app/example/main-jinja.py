from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path

# 절대 경로 설정
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# mount : 미들웨어
# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates 위치를 지정
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# router
@app.get("/")
async def hello():
    return "hello world"


# 요청시 들어오는 id, request의 순서는 상관없음
# 옆에 있는 Request, str과 같은 타입힌트로 알게됨
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    print(id)
    print(request["headers"])
    return templates.TemplateResponse(
        "index.html", {"request": request, "id": id, "data": "DATA"}
    )


# ValueError: context must include a "request" key
# TemlplateResponse안으로 html 변수를 보낼 때, request key가 필요함
