import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI(title="测试Demo")

# 父路由：去掉tags，只负责前缀拼接
main_router = APIRouter(prefix="/emn")
user_router = APIRouter(tags=["数据库请求"], prefix="/user")
item_router = APIRouter(tags=["元素个体"], prefix="/item")

main_router.include_router(user_router)
main_router.include_router(item_router)

# main_router自身接口手动分配tag
@main_router.get("/emn1", tags=["账号登录与注册"])
async def emn1():
    return {"message": "Hello World3"}

@main_router.get("/emn2", tags=["账号登录与注册"])
async def emn2():
    return {"message": "Hello World4"}

@item_router.get("/item1")
async def item1():
    return {"message": "Hello World1"}

@item_router.get("/item2")
async def item2():
    return {"message": "Hello World2"}

@user_router.get("/info")
async def user_info():
    return {"username": "test"}

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
