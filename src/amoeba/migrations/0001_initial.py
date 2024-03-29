# Generated by Django 2.2.6 on 2019-12-02 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('code', models.CharField(max_length=64, verbose_name='编码')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('category', models.IntegerField(choices=[(1, '资产'), (2, '负债')], default=1, verbose_name='类型')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='余额')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text='即成本中心段', max_length=64, verbose_name='名称')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='余额')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amoeba.Company', verbose_name='公司')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text='coa中的产品段', max_length=128, verbose_name='产品')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='余额')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amoeba.Company', verbose_name='产品')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='余额')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amoeba.Company', verbose_name='公司')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserExt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coa_credit', models.ForeignKey(help_text='用户常用的贷方科目', on_delete=django.db.models.deletion.CASCADE, related_name='userext_coa_credits_set', to='amoeba.Coa', verbose_name='贷方科目')),
                ('coa_debit', models.ForeignKey(help_text='用户常用的借方科目', on_delete=django.db.models.deletion.CASCADE, related_name='userext_coa_debit_set', to='amoeba.Coa', verbose_name='借方科目')),
                ('company', models.ForeignKey(help_text='用户记账所使用的默认公司', on_delete=django.db.models.deletion.CASCADE, to='amoeba.Company', verbose_name='公司')),
                ('department', models.ForeignKey(help_text='用户记账所使用的默认部门（成本中心）', on_delete=django.db.models.deletion.CASCADE, to='amoeba.Department', verbose_name='部门')),
                ('product', models.ForeignKey(help_text='用户记账所使用的默认产品', on_delete=django.db.models.deletion.CASCADE, to='amoeba.Product', verbose_name='产品')),
                ('project', models.ForeignKey(help_text='用户记账所使用的默认项目', on_delete=django.db.models.deletion.CASCADE, to='amoeba.Project', verbose_name='项目')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='JournalHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128, verbose_name='说明')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amoeba.Company', verbose_name='公司')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_dr', models.DecimalField(decimal_places=2, help_text='借方金额', max_digits=15, verbose_name='借方金额')),
                ('amount_cr', models.DecimalField(decimal_places=2, help_text='贷方金额', max_digits=15, verbose_name='贷方金额')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('coa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amoeba.Coa', verbose_name='科目')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amoeba.Department', verbose_name='部门')),
                ('head', models.ForeignKey(on_delete=models.Model, to='amoeba.JournalHead', verbose_name='日记账头')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amoeba.Product', verbose_name='产品')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amoeba.Project', verbose_name='项目')),
            ],
        ),
        migrations.AddField(
            model_name='coa',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amoeba.Company', verbose_name='公司'),
        ),
        migrations.AddField(
            model_name='coa',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amoeba.Coa', verbose_name='上级'),
        ),
    ]
