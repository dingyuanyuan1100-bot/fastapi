from enum import Enum
from typing import Annotated

import fastapi
import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel, BeforeValidator

app = FastAPI()
#Path请求
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(...,alias="item_id")):
    return {"item_id": item_id}

@app.get("/items1/{item_id}")
async def read_item(item_id: int = Path(...,gt=0,lt=100,alias="item_id")):
    return {
        "item_id": item_id
            }


#Path与pattern的组合用法
@app.get("/items2/{item_id}")
async def read_item(item_id: str = Path(...,pattern=r'^a\d+$', alias="item_id")):
    return {
        "item_id": item_id
            }


#请求体写法
class Item3(BaseModel):
    title: str
    price: float
    id:int
@app.get("/items3")
async def read_items(item:Item3):
    return {
        "item_id":item.id,
        "title":item.title,
        "price":item.price,
            }

#枚举写法
class Item4(str,Enum):
    asd = "asd"
    abc = "abc"
    asdf = "asdf"
@app.get("/items4/{item_id}")
async def read_item(item_id:Item4):
    return {
        "item_id":item_id
            }


#Annotated(官方推荐的声明式写法)
def ValidateItem(value):
    if not value.startswith("asd"):
        raise ValueError("请以 asd 开头")
    return value
#创建带验证的类型别名
Item6 = Annotated[str,BeforeValidator(ValidateItem)]
@app.get("/items6/{item_id}")
async def read_item(item_id:Item6):
    return {
        "item_id":item_id
    }



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)