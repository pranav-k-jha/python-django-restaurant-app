# Generated by Django 3.2.8 on 2021-11-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_ordermodel_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='zip_code',
            field=models.CharField(default='43701', max_length=7, verbose_name='zip code'),
        ),
    ]
