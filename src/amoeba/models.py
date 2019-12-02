from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.timezone import now
from django.contrib.auth.models import User

from typing import List, Tuple


# Create your models here.
class Company(TimeStampedModel):
    """公司"""

    def __str__(self):
        return f'{self.name}'

    name = models.CharField(max_length=128, verbose_name='名称')


class Coa(TimeStampedModel):
    """coa科目表"""

    def __str__(self):
        return f'{self.name}'

    code = models.CharField(max_length=64, verbose_name='编码')
    name = models.CharField(max_length=64, verbose_name='名称')
    category = models.IntegerField(verbose_name='类型', choices=((1, '资产'), (2, '负债')), default=1)
    balance = models.DecimalField(verbose_name='余额', default=0, max_digits=15, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='公司')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='上级', blank=True, null=True)


class Department(TimeStampedModel):
    """成本中心"""

    def __str__(self):
        return f'{self.name}'

    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='公司')
    name = models.CharField(max_length=64, verbose_name='名称', help_text='即成本中心段')
    balance = models.DecimalField(verbose_name='余额', default=0, max_digits=15, decimal_places=2)


class Project(TimeStampedModel):
    """项目"""

    def __str__(self):
        return f'{self.name}'

    company = models.ForeignKey(Company, verbose_name='公司', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name='名称')
    balance = models.DecimalField(verbose_name='余额', default=0, max_digits=15, decimal_places=2)


class Product(TimeStampedModel):
    """产品"""

    def __str__(self):
        return f'{self.name}'

    company = models.ForeignKey(Company, verbose_name='产品', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='产品', help_text='coa中的产品段')
    balance = models.DecimalField(verbose_name='余额', default=0, max_digits=15, decimal_places=2)


class UserExt(models.Model):
    """用户扩展表"""

    def __str__(self):
        return f'{self.id}'

    user = models.OneToOneField(User, verbose_name='用户', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name='公司', help_text='用户记账所使用的默认公司', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name='部门', help_text='用户记账所使用的默认部门（成本中心）',
                                   on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name='项目', help_text='用户记账所使用的默认项目', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='产品', help_text='用户记账所使用的默认产品', on_delete=models.CASCADE)
    coa_debit = models.ForeignKey(Coa, verbose_name='借方科目', help_text='用户常用的借方科目', on_delete=models.CASCADE,
                                  related_name='userext_coa_debit_set')
    coa_credit = models.ForeignKey(Coa, verbose_name='贷方科目', help_text='用户常用的贷方科目', on_delete=models.CASCADE,
                                   related_name='userext_coa_credits_set')


class Batch(TimeStampedModel):
    """日记批"""

    def __str__(self):
        return f'{self.name}'

    company = models.ForeignKey(Company, verbose_name='公司', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='说明', max_length=128)
    memo = models.TextField(verbose_name='备注', blank=True, null=True)

    @classmethod
    def default_batch_name(cls):
        return now().strftime('%Y%m%d%H%M')


class Journal(models.Model):
    """日记账"""

    def __str__(self):
        return f'{self.id}'

    batch = models.ForeignKey(Batch, on_delete=models.Model, verbose_name='批次')
    coa = models.ForeignKey(Coa, verbose_name='科目', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name='部门', blank=True, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name='项目', blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='产品', blank=True, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='金额', help_text='正数为借，负数为贷', max_digits=15, decimal_places=2)
    memo = models.TextField(verbose_name='备注', blank=True, null=True)
