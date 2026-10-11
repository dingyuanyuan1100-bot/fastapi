"""
同源策略 SOP & CORS 跨域资源共享
1. 同源策略（Same‑Origin Policy，SOP）
浏览器的安全机制，限制一个源的网页脚本访问另一个源的数据。

✅ 什么是「源 origin」
源由三部分全部相同才算同源：
1. 协议（`http` / `https`）
2. 域名（`example.com`）
3. 端口（`80`、`443`、`8080`）

如
`https://example.com:443` 和 `http://example.com:80`
👉 不同源：协议不一样、端口不一样。

🛡️ 同源策略作用
防止恶意网站的 JS 脚本，未经授权读取别的网站数据，保护用户隐私信息。
问题：现在前后端分离项目，前端页面和后端 API 经常不是同一个源，**业务需要跨源请求**，同源策略会直接拦截，于是就有了 CORS。

"""
from fastapi.responses import HTMLResponse

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

app = FastAPI()
app = FastAPI()

# 第一步：注册中间件！放在最前面
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 第二步：挂载静态资源
app.mount("/templates", StaticFiles(directory="templates", html=True), name="templates")

# 第三步：写接口路由
@app.get("/info")
async def root():
    return {
        "msg":"跳转成功"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)