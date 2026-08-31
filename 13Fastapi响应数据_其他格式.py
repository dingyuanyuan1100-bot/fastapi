from markupsafe import escape
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/string1")
async def string1():
    return "hello world"

@app.get("/string2")
async def string2():
    return "<html><h1>111</h1></html>"

#重定向跳转并传递参数
@app.get("/string3")
async def string3(name:str):
    return RedirectResponse(
        f"/string4?name={name}",
    )
@app.get("/string4")
async def string4(name:str):
    name = escape(name)     #转义 < > " ' 等符号，防止XSS跨站脚本攻击
    return HTMLResponse(
        f"""
        <html>
            <h1>跳转成功</h1>
            <h2>我是{name}</h2>
        </html>
        """
    )
#挂载HTML目录
app.mount('/templates', StaticFiles(directory='templates',html=True))
app.mount('/statics', StaticFiles(directory='statics'))

if __name__ == '__main__':
    uvicorn.run(app="13Fastapi响应数据_其他格式:app", host='127.0.0.1', port=8000)