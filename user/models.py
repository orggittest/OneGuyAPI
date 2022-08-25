from django.db import models
from common import YGBaseModel


class AppUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(~models.Q(status=2))


# Create your models here.
class AppUser(YGBaseModel):
    name = models.CharField(max_length=20, verbose_name='用户名')
    auth_key = models.CharField(max_length=100, verbose_name='口令')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    create_time = models.DateField(auto_now_add=True, verbose_name='注册时间')
    status = models.IntegerField(default=0, choices=((0, '未激活'), (1, '正常'), (2, '注销')), verbose_name='状态')

    img1 = models.CharField(max_length=100, verbose_name='头像', null=True, blank=True)
    objects = AppUserManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_app_user'
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name
