# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# FastAPI 앱 인스턴스 생성
app = FastAPI()


# --- 데이터 모델 정의 (Pydantic) ---
# 요청 본문(request body)의 데이터 구조를 정의합니다.
# 자동으로 데이터 유효성 검사 및 문서화가 이루어집니다.
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    is_offer: bool | None = None


# --- 간단한 인메모리 데이터베이스 ---
# 실제로는 Cloud SQL 같은 데이터베이스를 사용해야 합니다.
# 여기서는 테스트를 위해 Python 딕셔너리를 사용합니다.
db: Dict[int, Item] = {}


# --- API 엔드포인트 정의 ---

@app.get("/")
def read_root():
    """
    서버가 살아있는지 확인하는 기본 엔드포인트입니다.
    """
    return {"message": "FastAPI 서버가 정상적으로 동작 중입니다."}


@app.post("/items/{item_id}", status_code=201)
def create_item(item_id: int, item: Item):
    """
    새로운 아이템을 데이터베이스에 생성합니다.
    - Path Parameter: item_id
    - Request Body: Item 모델
    """
    if item_id in db:
        raise HTTPException(status_code=400, detail=f"Item with ID {item_id} already exists.")
    db[item_id] = item
    return {"item_id": item_id, **item.model_dump()}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    특정 아이템의 정보를 조회합니다.
    - Path Parameter: item_id
    """
    if item_id not in db:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found.")
    return db[item_id]


@app.get("/items/")
def read_all_items():
    """
    데이터베이스에 있는 모든 아이템 목록을 조회합니다.
    """
    return db