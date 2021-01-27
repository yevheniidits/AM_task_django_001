# Generated by Django 3.1.5 on 2021-01-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=50, verbose_name='Производитель'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
    ]