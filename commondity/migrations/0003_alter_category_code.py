# Generated by Django 4.0.6 on 2022-08-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondity', '0002_alter_category_parent_alter_category_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=20, verbose_name='编码'),
        ),
    ]
