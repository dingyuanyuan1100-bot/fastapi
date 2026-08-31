import asyncio
from tortoise import Tortoise
from tortoise_config import TORTOISE_ORM

async def check():
    await Tortoise.init(config=TORTOISE_ORM)
    conn = Tortoise.get_connection("default")
    desc = await conn.execute_query("DESC users")
    print("users 表结构:")
    for row in desc[1]:
        print(f'  {row["Field"]:12} {row["Type"]:20} {row["Null"]:5} {row["Key"]:5}')
    hist = await conn.execute_query("SELECT * FROM aerich")
    print()
    print("aerich 迁移记录:")
    for row in hist[1]:
        print(f'  id={row["id"]} version={row["version"]} app={row["app"]}')
    await Tortoise.close_connections()

asyncio.run(check())
