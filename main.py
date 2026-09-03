#ORM基础配置
import uvicorn
from fastapi import FastAPI
from typing import Dict

app = FastAPI()
TORTOISE_ORM: Dict={
    #开发环境使用SQLite(基于文件，无需服务器)
    #“default”:"sqlite//db.sqlite3"
    #开发环境使用Mysql
    "connections":{"default":"mysql://root:123456@127.0.0.1:3306/fastapi_db2"},
    "apps":{
        "models": {
            #模型模块和 Aerich 迁移模块
            "models": ["model.model2","aerich.models"],
            "default_connection": "default",
        }
    },
    #连接池配置（推荐）
    "use_tz":False,         #是否使用时区
    "timezone":"UTC",       #默认时区
    "db_pool":{
        "max_size":10,      #最大连接数
        "min_size":1,       #最小链接数
        "idle_timeout":30   #空闲连接超时（秒）
    }
}
from tortoise.contrib.fastapi import RegisterTortoise  # Tortoise‑ORM 专门给 FastAPI 封装的集成工具函数

RegisterTortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,          #开发环境自动生成表结构
    add_exception_handlers=True,    #添加默认异常处理
)




if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

"""
# 1.初始化aerich（生成迁移文件夹、读取pyproject.toml配置）
aerich init -t "在执行这个指令终端到nodel的相对路径"   生成的迁移文件在当前终端下面(注意中文乱码问题！！！)

# 2.初始化数据库，根据模型生成表结构，生成初始迁移文件
aerich init-db   #注意是英文减号不是-

# 3.模型改动后，生成迁移脚本（相当于makemigrations）
aerich migrate --name "注释"  （改变迁移迁移模型后才生效）

# 4.执行迁移，更新数据库表（相当于migrate）
aerich upgrade

# 5.回滚到指定版本，降级
aerich downgrade --version 版本号

# 6.查看迁移历史
aerich history  需要先装 pip install cryptography

# 7.查看还没执行的迁移
aerich heads

# 8.反向：把数据库现有表逆向生成Tortoise模型代码
aerich inspectdb


"""