from fastapi import FastAPI, Request
import json

app = FastAPI()

# 1.GET接口：只能拿url、ip、header、query、cookie，不能读body相关(json/form/files)
@app.get('/client-info')
async def client_info_get(request: Request):
    return {
        "请求URL": str(request.url),
        "请求方法": request.method,
        "请求IP": request.client.host if request.client else None,
        "请求参数": dict(request.query_params),
        "请求头": dict(request.headers),
        "请求cookies": dict(request.cookies),
        "请求path_params": dict(request.path_params),
    }

# 2.POST接口，处理body
@app.post('/client-info')
async def client_info_post(request: Request):
    req_json = None
    req_form = None
    req_files = []
    return {
        "请求URL": str(request.url),
        "请求方法": request.method,
        "请求IP": request.client.host if request.client else None,
        "请求参数": dict(request.query_params),
        "请求头": dict(request.headers),
        "请求json": req_json,
        "请求cookies": dict(request.cookies),
        "请求form": dict(req_form) if req_form else None,
        "请求files": req_files,
        "请求path_params": dict(request.path_params),
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='08Fastapi请求对象Request:app', host='127.0.0.1', port=8000, reload=True)
