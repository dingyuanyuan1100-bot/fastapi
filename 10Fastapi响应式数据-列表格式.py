import math
import time
from typing import Optional

import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int          # 补上id字段
    name: str
    price: float
    category: str


#批量创建10个Item类
DB = [
    Item(id=i, name=f"Apple{i}", price=100*i, category="ipad" if i%2==0 else "other")
    for i in range(10)
]


@app.get("/items1")
async def items1():
    return [
        "apple1",
        "apple2",
        "apple3"
    ]


@app.get("/items2")
async def items2():
    return DB


@app.get("/items3")
async def items3(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页数量"),
    category: Optional[str] = Query(None, description="分类")
):
    #数据过滤
    filter_items = DB
    if category:
        # Item是pydantic对象，用 .属性 不要[]字典取值
        filter_items = [item for item in filter_items if item.category == category]

    total = len(filter_items)
    total_page = math.ceil(total / page_size)

    #分页切片
    start = (page - 1) * page_size
    end = start + page_size
    page_data = filter_items[start:end]

    return {
        "templates": page,
        "page_size": page_size,
        "total": total,
        "total_page": total_page,
        "data": page_data
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
