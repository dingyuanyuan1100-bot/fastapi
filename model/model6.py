import uvicorn
from fastapi import FastAPI
from tortoise import Tortoise, models, fields, run_async
from tortoise.contrib.fastapi import register_tortoise


#作者主表
class Author(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    #作者——作者详情(一对一)
    Author_Detail = fields.OneToOneField("models.AuthorDetail", on_delete=fields.CASCADE,related_name="author")

#作者详情
class AuthorDetail(models.Model):
    id = fields.IntField(pk=True)
    born = fields.DateField()
    detail = fields.CharField(max_length=20)

#作者图书
class Book(models.Model):
    id = fields.IntField(pk=True)
    book_title = fields.CharField(max_length=20)
    #图书——作者（一对多）
    Book_Author = fields.ForeignKeyField( "models.Author", on_delete=fields.CASCADE, related_name="books")
    #图书对分类（多对多）
    categories = fields.ManyToManyField( "models.Category", related_name="books",through="BookCategory")

#图书分类
class Category(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)

#图书-分类中间表
class BookCategory(models.Model):   #Tortoise 会自动生成 id 主键，不用手动写
    book = fields.ForeignKeyField("models.Book", on_delete=fields.CASCADE, )
    category = fields.ForeignKeyField("models.Category", on_delete=fields.CASCADE)
    add_time = fields.DatetimeField(auto_now_add=True)
    class Meta:
        unique_together = ("book", "category")
async def init():
    await Tortoise.init(
        db_url="mysql://root:123456@127.0.0.1:3306/text1",
        modules={"models":["model.model6"]},
    )
    await Tortoise.generate_schemas(safe=True)


