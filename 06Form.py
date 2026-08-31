from typing import Annotated

import uvicorn
from fastapi import FastAPI,Form
from pydantic import BaseModel

app = FastAPI()
@app.post("/login1")
async def create_item( name:str = Form(...), password: str = Form(...) ):
    return {"name": name, "password": password}


class User1(BaseModel):
    name: str
    password: str
@app.post("/login2")
async def create_item( user : Annotated[ User1 ,Form()]):
    return user



if __name__ == '__main__':
    uvicorn.run(app="06Form:app", host="0.0.0.0", port=8011, reload=True)