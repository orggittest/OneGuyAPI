# Generated by Django 4.0.6 on 2022-08-22 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondity', '0003_alter_category_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]