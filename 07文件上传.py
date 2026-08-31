import asyncio
import uvicorn
from fastapi import FastAPI,File,UploadFile,HTTPException
import aiofiles
from pathlib import Path, PurePath

app = FastAPI()
#简单文件上传
@app.post("/file")
async def file1(file:bytes= File(...)):
    with open('data1/file.jpg', 'wb') as f:
        f.write(file)
    return {'file':"上传成功"}

#异步分片处理（UploadFile,aipfile））单一文件上传
@app.post("/file1")
async def file2(file: UploadFile = File(...)):
    async with  aiofiles.open('data1/file.jpg', 'wb') as f:
        while True:
            chunk = await file.read(1024*1024)
            if not chunk:
                break
            await f.write(chunk)
#异步分片处理（UploadFile,aipfile））多文件上传
async def get_file(file):
    raw_name = file.filename
    safe_filename = Path("./data1")
    path_file = safe_filename / raw_name
    async with aiofiles.open(path_file, 'wb') as f:
        while True:
            chunk = await file.read(1024 * 1024)
            if not chunk:
                break
            await f.write(chunk)

@app.post("/file2")
#多文件写法（UploadFile）
async def file3(files: list[UploadFile] = File(...)):
    tasks = [get_file(file) for file in files ]
    await asyncio.gather(*tasks)
    return {
        "msg":"请求完成"
    }


if __name__ == "__main__":
    uvicorn.run(app="07文件上传:app", host="127.0.0.1", port=8000, reload=True)
