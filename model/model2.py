from tortoise.models import Model
from tortoise.fields import CharField, DatetimeField, DateField, BooleanField, IntField


class User1(Model):
    id = IntField(pk=True,max_length=20,description="学生ID,主键")
    username = CharField(max_length=20,unique=True)
    age = IntField(default=0)
    email = CharField(max_length=20,unique=True,null=True,description="学生邮箱，唯一")
    class Meta:
        table = "students"


    def __str__(self):
        return f"Student {self.username},Age:{self.age},Email:{self.email}"