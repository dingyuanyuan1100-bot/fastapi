from tortoise.models import Model
from tortoise.fields import CharField, DatetimeField, BooleanField

class User(Model):
    # 主键，UUID字符串，长度36
    id = CharField(max_length=36, pk=True)
    # 用户名，最大50字符，唯一不重复
    username = CharField(max_length=50, unique=True)
    # 邮箱，最大255字符，唯一
    email = CharField(max_length=255, unique=True)
    # 是否激活，默认True
    is_active = BooleanField(default=True)
    # 创建时间：对象第一次插入数据库时自动填充时间
    created_at = DatetimeField(auto_now_add=True)
    # 更新时间：每次对象保存修改，自动更新为当前时间
    updated_at = DatetimeField(auto_now=True)
    # 手机号码
    ipone = CharField(max_length=11, null=True)

    class Meta:
        table = "users"  # 自定义数据库表名
        ordering = ["-created_at"]  # 默认查询排序，`-`代表降序，最新创建排在前面

    def __str__(self):
        return self.username

