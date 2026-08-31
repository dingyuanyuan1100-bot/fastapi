import uvicorn
from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#Field主要用于Json请求体验证
class User(BaseModel):
    id: str = Field(default_factory = lambda: str(uuid4()) )
    name : str = Field(...)
    age : int = Field(...,ge = 18)
    email : str = Field(...)
    @field_validator('email')
    def email_test(cls,v):
        if '@' not in v:
            raise ValueError("邮箱格式错误")
        return v
@app.post("/items1")
async def read_items1(item_id: User):
    return {
        "id": item_id.id,
        "neme": item_id.name,
        "age": item_id.age,
        "email": item_id.email
    }


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8010)