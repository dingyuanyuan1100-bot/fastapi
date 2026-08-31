import asyncio
import time
import uvicorn
from fastapi import FastAPI

app = FastAPI()

#异步5个5s的任务
@app.get("/test1")
async def test1():
    start = time.time()
    task = [ asyncio.sleep(5) for i in range(10) ]
    await asyncio.gather(*task)
    end = time.time()
    return end-start

#同步5个5s的任务
@app.get("/test2")
async def test2():
    start = time.time()
    for i in range(10):
        time.sleep(5)
    end = time.time()
    return end-start
if __name__ == '__main__':
    uvicorn.run(app="Fastapi异步处理:app", host='0.0.0.0', port=8000)