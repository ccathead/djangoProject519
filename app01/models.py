from datetime import timezone

from django.db import models


# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=32,default="用户")
    password = models.CharField(verbose_name="密码", max_length=64,default="<PASSWORD>")
    age = models.IntegerField(verbose_name="年龄", default=0)
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name="入职时间")
    create_time = models.DateField(verbose_name="入职时间")
    depart_id = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)  # 级联删除
    gender_choices = {
        (1, "男"),
        (2, "女")
    }
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
