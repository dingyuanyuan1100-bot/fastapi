from typing import List

import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


@app.get("/test")
async def test():
    return {"hello": "world"}


class Item(BaseModel):
    id: int
    name: str
    price: float
    category: str



# 模拟数据库100条数据
DB = [
    Item(id=i, name=f"Apple{i}", price=i*100.0, category="ipone" if i % 2 == 0 else "car")
    for i in range(1, 101)
]


# 分类过滤接口
@app.get("/db")
async def db(category: str = Query(None, description="分类(car,ipone)")):
    temp = DB
    if category:
        temp = [item for item in DB if item.category == category]
    return temp


class Response(BaseModel):
    status: str = "success"
    data: List[Item]

# 过滤 + 分页接口
@app.get("/file_page")
async def file_page(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页数量"),
    category: str = Query(None, description="分类")
):
    # 1.先过滤
    file_items = DB
    if category:
        file_items = [item for item in file_items if item.category == category]

    total = len(file_items)
    total_page = (total + page_size - 1) // page_size  # 向上取整总页数( 不能用total//page_size+1 )
    offset = (page - 1) * page_size
    data = file_items[offset: offset + page_size] #切片写法

    # 返回分页完整结构：数据 + 分页信息
    return {
        "templates": page,
        "page_size": page_size,
        "total": total,
        "total_page": total_page,
        "data": data
    }


if __name__ == '__main__':
    uvicorn.run(app="11数据过滤与分页:app", host="127.0.0.1", port=8000)
