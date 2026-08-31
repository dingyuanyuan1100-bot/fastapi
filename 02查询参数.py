from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#路径查询
@app.get("/query")
async def read_item(item_id: int, q: str):
    return {
        "item_id": item_id,
        "q": q
    }

#请求头请求
class Item(BaseModel):
    item_id: int
    description: str
    price: float
@app.post("/Item")
async def read_item(item: Item):
    return {
        "item_id": item.item_id,
        "description": item.description,
        "price": item.price
            }

#接收数据(支持多种数据类型的写法 Union )
@app.get("/items1/{item_id}")
async def read_item(item_id: Union[int, str] = None ):
    return {
        "item_id": item_id
            }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)