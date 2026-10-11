from datetime import date

import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from model.model6 import Author, Book, Category,AuthorDetail,BookCategory
app = FastAPI()

register_tortoise(
    app,
    db_url="mysql://root:123456@127.0.0.1:3306/text1",
    modules={"models": ["model.model6"]},
    generate_schemas=True,          # 自动建表(已存在则跳过)
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/create_author")
async def create_author(name: str, born: date, detail: str, book_title: str, category: str):
    d = await AuthorDetail.create(born=born, detail=detail)
    author = await Author.create(name=name, Author_Detail=d)

    book = await Book.create(book_title=book_title, Book_Author=author)

    cat = await Category.create(name=category)
    await BookCategory.create(book=book, category=cat)   # .add() 不带 add_time,需手动插中间表

    a = await Author.get(id=author.id).prefetch_related("Author_Detail", "books__categories")
    return {
        "text":a,
        "author": a.name,
        "born": a.Author_Detail.born,
        "books": [b.book_title for b in a.books],
        "categories": [c.name for c in a.books[0].categories],
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)