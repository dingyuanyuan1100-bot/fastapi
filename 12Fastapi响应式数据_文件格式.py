from sys import path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response, FileResponse, StreamingResponse

app = FastAPI()

#下载txt格式
@app.get("/download_text")
async def custom_file():
    info = b'asf'
    return Response(
        content=info,
        media_type="text/plain",#告诉浏览器，格式为text
        #不在线浏览 ，下载 attachment 下载后的文件名为 file.txt
        headers={
        "Content-Disposition":'attachment; filename="file.txt"'
        }
    )

#下载pdf格式
@app.get("/download_pdf")
async def custom_file2():
    path = r"C:\Users\Administrator\Desktop\统252班武子俊259104552.pdf"
    #FileResponse 独属于文件的上传格式
    return FileResponse(
        path = path,
        media_type="application/pdf",#告诉浏览器，格式为pdf
        # 不在线浏览 ，下载 attachment 下载后的文件名为 file.pdf
        headers={
            "Content-Disposition":'attachment; filename="file.pdf"'
        }
    )

#下载mp3格式
@app.get("/download_mp3")
async def custom_file3():
    path = r"C:\Users\Administrator\Desktop\01.mp3"
    return FileResponse(
        path = path,
        media_type="audio/mpeg",
        headers={
            "Content-Disposition":'attachment; filename="file.mp3"'
        }
    )

#下载mp4格式(老写法)
def check(path:str ,chunk_size=1024*1024*10):
    with open(path, 'rb') as f:
        chunk = f.read(chunk_size)
        while chunk:
            yield chunk
            chunk = f.read(chunk_size)
#下载mp4格式(新写法，海象运算符写法)
def check(path:str ,chunk_size=1024*1024*10):
    with open(path, 'rb') as f:
        while chunk:= f.read(chunk_size):
            yield chunk



@app.get("/download_mp4")
async def custom_file4():
    path = r"C:\Users\Administrator\Downloads\小奶猫玩耍_爱给网_aigei_com.mp4"
    return StreamingResponse(
        content=check(path,chunk_size=1024*1024*10),
        media_type="video/mp4",
        headers={
            "Content-Disposition":'attachment; filename="file.mp4"'
        }
    )

if __name__ == "__main__":
    uvicorn.run(app="12Fastapi响应式数据_文件格式:app", host="127.0.0.1", port=8000)