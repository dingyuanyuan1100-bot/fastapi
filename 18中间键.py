from fastapi.requests import Request

import uvicorn
from fastapi import FastAPI

app = FastAPI()

#中间件只要收到请求就处理
@app.middleware("http")
async def middleware_1(request: Request, call_next):
    print("中间件处理1前")
    response = await call_next(request)
    print("中间件处理1后")
    return response

@app.middleware("http")
async def middleware_2(request: Request, call_next):
    print("中间件处理2前")
    response = await call_next(request)
    print("中间件处理2后")
    return response

#中间件写法2

"""
scope、receive、send 
是 ASGI 协议标准参数，FastAPI/Starlette 底层是 ASGI，所有类中间件 async def __call__(self, scope, receive, send) 都是这三个参数。
@app.middleware("http") 装饰器已经封装好了，直接给Request、call_next，看不到这三个底层参数
"""
class middleware_3():
    def __init__(self,app):
        self.app = app
    async def middleware(self,scope,receive,send):
        print("中间件处理3前")
        await self.app(scope,receive,send)
        print("中间件处理3后")
#添加类中间件
app.add_middleware(middleware_3)


@app.get("/text1")
async def index():
    print("处理中")
    return {"hello": "world"}





if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)