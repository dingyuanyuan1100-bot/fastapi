import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypeVar, Generic, Union

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

    #默认 list类型，里面只能填字符串 ， =[]  默认为空
    tags:list[str] = []

#返回 return {"name":"张三","age":18}
@app.get("/items/dict")
async def read_item1():
    return {
        "name":"张三",
        "age":18
    }
#返回 return {"id": 1,"name": "李四","tags": []}(必须按照规范的 Item 格式来搞)
@app.get("/items/model")
async def read_item2():
    return Item(
        id=1,
        name="李四"
    )
#加上 response_model_exclude_unset=True 返回 return {"id": 1,"name": "王五"}
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item3():
    return  Item(
        id=1,
        name="王五"
    )

# 定义泛型模型
T = TypeVar("T")
#正确返回
class SuccessResponse(BaseModel, Generic[T]):
    status: str = "success"
    data: T

#错误返回
class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
    code: int

@app.post("/items1/{item_id}", response_model=Union[SuccessResponse[Item],ErrorResponse])
async def read_item4(item_id: int):
    if item_id == 1:
        item = Item( id = 1,name = "张三" , tags=["apple","banana"] )
        #`SuccessResponse` 是 Pydantic 模型，要传关键字参数.不写`data=`，会把`item`传给第一个位置参数`status`，直接报错
        return SuccessResponse(data= item)
    else:
        return ErrorResponse( message="id错误",code=400 )



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)