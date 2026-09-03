"""
Python字段	            数据库类型	        用途	                    必选 / 常用参数
fields.CharField	    VARCHAR	            短字符串（用户名、邮箱）	max_length必填，unique=True唯一，index=True索引
fields.TextField	    TEXT	            大段长文本、文章内容	    null=True允许为空
fields.IntField	        INTEGER         	普通整数	                pk=True设为主键，default=0默认值
fields.BigIntField	    BIGINT	            大整数，id 雪花 id 等大数	pk=True
fields.FloatField	    DOUBLE	            浮点数	                ⚠️不要存金额，浮点精度丢失
fields.DecimalField	    DECIMAL	            金额高精度小数	            max_digits总位数，decimal_places小数位数
fields.BooleanField	    BOOLEAN	            布尔开关	                default=True / False
fields.DateField	    DATE	            只存日期 2026‑08‑31	    auto_now=True保存自动更新日期
fields.DatetimeField	DATETIME/TIMESTAMP	日期 + 时间	            auto_now_add=True创建时写入；auto_now=True每次更新刷新
fields.JSONField	    JSON/JSONB	        存字典、列表	            encoder/decoder自定义编解码
fields.UUIDField	    UUID/CHAR(36)	    UUID 唯一标识	        做主键自动生成 UUID4
fields.BinaryField	    BLOB	            原始二进制字节	            不支持过滤查询

"""
"""
from tortoise.models import Model
from tortoise import fields  # 所有字段都从这里导入

class User(Model):
    # 在这里定义字段
    
    class Meta:
        table = "auth_users"                            # 指定数据库真实表名
        ordering = ["-created_at"]                      #默认查询排序，`-`代表倒序
        unique_together = [("name", "date")]            # 联合唯一约束 a或b可以重复，a+b不能重复
        indexes = [("location",)]                       # 联合/单字段索引
        ordering = ["-date", "name"]                    # 默认查询排序
"""