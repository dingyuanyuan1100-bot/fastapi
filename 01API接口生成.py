from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

#面对冲突，只支持最前的请求
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id1": item_id}

#传递多值
@app.get("/items1/{item_id}/{name}")
def read_item(item_id: int, name: str):
    return {"item_id1": item_id, "item_id2": name}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8011)
