# Generated by Django 4.0.6 on 2022-08-21 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='编码')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('grade', models.IntegerField(default=1, verbose_name='等级')),
                ('picture_url', models.CharField(max_length=200, verbose_name='图片地址')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondity.category', verbose_name='父类')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
                'db_table': 't_category',
            },
        ),
    ]