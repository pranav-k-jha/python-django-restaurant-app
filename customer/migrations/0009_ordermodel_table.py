# Generated by Django 3.2.8 on 2021-11-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_ordermodel_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='table',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
