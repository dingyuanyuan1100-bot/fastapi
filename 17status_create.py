import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from model.model2 import User1


from tortoise.exceptions import IntegrityError


async def create_user(username: str, age : int = None, email : str = None):
    stu = User1(username=username, age=age, email=email)
    try:
        await stu.save()
        return stu
    except IntegrityError as e:   # unique=True 的字段重复时,数据库会拒绝插入并抛这个异常
        print("注册失败:", e)
        return None

async def review_user(stu_id: int, name:str,age:int,email:str) -> User1:
    try:
        stu = await User1.get(id=stu_id)  #查不到会爆错
    except:
        return "无该账户"
    print(stu)
    if name:
        stu.username = name
    if age:
        stu.age = age
    if email:
        stu.email = email
    await stu.save()
    return stu

async def get_stuexcel(name: str) -> list[User1]:
    stu = await User1.filter(username=name)
    if stu:
        return stu

async def get_stuxcel_age(age: int) -> list[User1]:
    stu = await User1.filter(age=age)  #使用get要注意多个或零个会爆错
    if stu:
        return stu

async def get_stu(name: str) -> list[User1]:
    stu = await User1.filter(username__contains=name)  # 1.x 语法:双下划线
    if stu:
        return stu

async def del_stu(id:int = None ,name: str = None):
    # get_or_none:查不到返回 None 而不是抛 DoesNotExist 异常
    stu = None
    if id:
        stu = await User1.get_or_none(id=id)
    elif name:
        stu = await User1.get_or_none(username=name)
    if stu:
        print("删除:", stu)
        await stu.delete()
        return {"deleted": stu.username, "id": stu.id}
    return {"deleted": None, "msg": "未找到该用户"}

# tortoise-orm 1.x:小写的 register_tortoise 会把 ORM 初始化挂到 app 的 lifespan 上
# (大写 RegisterTortoise 直接调用不会初始化,必须配合 async with 使用)
app = FastAPI()

register_tortoise(
    app,
    db_url="mysql://root:123456@127.0.0.1:3306/fastapi_db1",
    modules={"models": ["model.model2"]},
    generate_schemas=True,          # 自动建表(已存在则跳过)
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

#注册账号
@app.get("/user_create",description="注册")
async def add_user(username: str, age: int = None, email: str = None):
    stu = await create_user(username, age, email)
    if stu is None:
        return {"code": 400, "msg": "注册失败:用户名或邮箱已被占用"}
    return {"code": 200, "id": stu.id, "username": stu.username, "age": stu.age, "email": stu.email}

#修改账号数据
@app.get("/user_review",description="修改账户")
async def check_user(id: int, name: str = None, age: int = None, email: str = None):
    stu = await review_user(id, name, age, email)
    return stu
#模糊查询
@app.get("/stu_get",description="模糊查询")
async def get_stu1(name: str):
    stu = await get_stu(name)
    return stu
#精确查询
@app.get("/stu_getexcel_name",description="精确查询名字")
async def get_stu2(name: str):
    stu = await get_stuexcel(name)
    return stu
#精确查询 年龄
@app.get("/stu_getexcel_age",description="精确查询年龄")
async def get_stu3(age:int):
    stu = await get_stuxcel_age(age)
    return stu

#删除账户
@app.get("/stu_del",description="账户删除")
async def delete_user(id: int = None , name: str = None):
    stu = await del_stu(id,name)
    return stu

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8004)