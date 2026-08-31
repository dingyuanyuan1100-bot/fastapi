import uvicorn
from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/items")
# ... 必填
async def read_items( id = Query(...) ):
    return {
        id:id
    }
# None 选填
@app.get("/items1")
async def read_items( id = Query(None) ):
    return {
        id:id
    }
#限制长度
@app.get("/items2")
async def read_items( id = Query(...,min_length=2,max_length=10) ):
    return {
        id:id
    }
#限制数值大小
@app.get("/items3")
async def read_items( id :int = Query(...,gt=2,lt=10) ):
    return {
        "id":id
    }
#参数别名写法（对内 id_item,对外 id））
@app.get("/items4/")
async def read_items( item_id: int = Query(...,gt=2,lt=10 ,alias="_id")):
    return {
        "item_id":item_id
    }
#正则匹配写法(pattern 写法)
@app.get("/items5")
async def read_items( item_id:str = Query(...,pattern=r'^a\d[1-5]+$',alias="_id") ):
    return {
        "item_id":item_id
    }
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)