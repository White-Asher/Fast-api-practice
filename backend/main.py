from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)

# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}

# alembic 없이 테이블 생성하기
# main.py 파일에 다음의 문장을 삽입하면 FastAPI 실행시 필요한 테이블들이 모두 생성된다.
# import models
# from database import engine
# models.Base.metadata.create_all(bind=engine)